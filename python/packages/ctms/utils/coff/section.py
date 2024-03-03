from .entries import *

class CoffSection:
	_idx:   int
	_name:  str
	_dimg:  memoryview
	_dview: memoryview
	_ent:   COFFSECTIONENTRY

	def __init__(self, idx: int, ent: COFFSECTIONENTRY, dimg: memoryview):
		self._idx  = idx
		self._ent  = ent
		self._dimg = dimg
		self._name = get_name(dimg, ent.naddr, ent.nlen)

	def write_n(self, offset: int = 0, value: int = 0, dlen: int = 4) -> None:
		"""
		Encodes a number into a specified number of bytes and writes it to the section data at a
		specified offset

		Args:
			offset: The offset into the section data to write to
			value:  The number value to write
			dlen:   The number of bytes to encode the value into
		"""
		self.data[offset:offset+dlen] = value.to_bytes(dlen, 'little')

	def write_n16(self, offset: int = 0, value: int = 0) -> None:
		"""
		Encodes a number into 2 bytes and writes it to the section data at a specified offset

		Args:
			offset: The offset into the section data to write to
			value:  The number value to write
		"""
		self.write_n(offset, value, 2)

	def write_n32(self, offset: int = 0, value: int = 0) -> None:
		"""
		Encodes a number into 4 bytes and writes it to the section data at a specified offset

		Args:
			offset: The offset into the section data to write to
			value:  The number value to write
		"""
		self.write_n(offset, value, 4)

	@property
	def name(self) -> str:
		"""
		Gets the name of the section

		Returns:
			The name of the section
		"""
		return self._name
	
	@property
	def phys_addr(self) -> int:
		"""
		Gets the physical address of the section within target memory

		Returns:
			The physical address of the section within target memory
		"""
		return self._ent.phys_addr
	
	@property
	def virt_addr(self) -> int:
		"""
		Gets the virtual address of the section within target memory

		Returns:
			The virtual address of the section within target memory
		"""
		return self._ent.virt_addr
	
	@property
	def flags(self) -> int:
		"""
		Gets the flags for the section

		Returns:
			The flags for the section
		"""
		return self._ent.flags
	
	@property
	def data(self) -> memoryview:
		"""
		Gets the data for the section

		Returns:
			The data for the section
		"""
		try:
			return self._dview
		except:
			addr        = self._ent.daddr
			dlen        = self._ent.dlen
			self._dview = self._dimg[addr:addr+dlen]
			return self._dview