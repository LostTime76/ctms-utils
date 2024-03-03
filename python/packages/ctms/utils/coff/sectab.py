from ctypes import *
from typing import Iterable
from .entries import COFFIMAGEENTRY, COFFSECTIONENTRY
from .section import CoffSection
from .. import clib

class CoffSectionTable:
	_pdata: Array[c_char]
	_ents:  Array[COFFSECTIONENTRY]
	_sects: list[CoffSection]
	_tab:   dict[str, CoffSection]

	def __init__(self, coff: COFFIMAGEENTRY, pdata: Array[c_char], dimg: memoryview):
		self._pdata = pdata
		self._ents  = CoffSectionTable._load_ents(coff)
		self._sects = CoffSectionTable._load_sects(self._ents, dimg)
		self._tab   = CoffSectionTable._load_tab(self._sects)

	def copy_to(self, taddr: int, data: bytearray) -> None:
		"""
		Copies all of the section data within the table to a bytearray that corresponds to a target
		memory range

		Args:
			taddr: The target memory address that corresponds to the start of the bytearray
			data:  The bytearray to copy the section data to
		"""
		clib.coff_copy_sects(
			taddr,
			len(data),
			self._pdata,
			clib.to_ptr(data),
			self._ents,
			len(self._ents))

	def _load_ents(coff: COFFIMAGEENTRY):
		ents = (COFFSECTIONENTRY * coff.sect_ents)()
		if not clib.coff_sects(byref(coff), ents):
			clib.error()
		return ents
	
	def _load_sects(ents: Array[COFFSECTIONENTRY], dview: memoryview) -> list[CoffSection]:
		sects = []
		for idx in range(len(ents)):
			sects.append(CoffSection(idx, ents[idx], dview))
		return sects
	
	def _load_tab(sects: list[CoffSection]) -> dict[str, CoffSection]:
		tab = {}
		for sect in sects:
			name = sect.name
			if name in tab:
				raise KeyError(f'The image contains a duplicate section \'{name}\'.')
			tab[name] = sect
		return tab
	
	def __getitem__(self, key: int | str):
		return self._sects[key] if isinstance(key, int) else self._tab[key]
	
	def __iter__(self) -> Iterable[CoffSection]:
		return iter(self._sects)