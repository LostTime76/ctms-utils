from ctypes import *
from .entries import COFFIMAGEENTRY
from .sectab import CoffSectionTable
from .. import clib

class CoffImage:
	_ent:   COFFIMAGEENTRY
	_sects: CoffSectionTable

	def __init__(self, data: bytearray):
		self._dview = memoryview(data)
		self._pdata = (c_char * len(data)).from_buffer(data)
		self._ent   = CoffImage._load(self._pdata)

	def _load(data: Array[c_char]) -> COFFIMAGEENTRY:
		entry = COFFIMAGEENTRY()
		if not clib.coff_load(data, len(data), byref(entry)):
			clib.error()
		return entry
	
	@property
	def entry(self) -> int:
		"""
		Gets the address of the first code instruction within target memory

		Returns:
			The address of the first code instruction within target memory
		"""
		return self._ent.entry
	
	@property
	def sects(self) -> CoffSectionTable:
		"""
		Gets the section table for the image

		Raises:
			Exception: If there was an error loading the table

		Returns:
			The section table for the image
		"""
		try:
			return self._sects
		except:
			self._sects = CoffSectionTable(self._ent, self._pdata, self._dview)
			return self._sects