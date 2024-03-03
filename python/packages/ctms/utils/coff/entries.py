from ctypes import *

class COFFIMAGEENTRY(Structure):
	target_id: int
	sect_ents: int
	entry:     int

	_fields_ = [
		('data', c_char_p),
		('dlen', c_int32),
		('target_id', c_int16),
		('sect_ents', c_int16),
		('entry', c_int32),
		('strtab_addr', c_int32)
	]

class COFFSECTIONENTRY(Structure):
	naddr:     int
	nlen:      int
	phys_addr: int
	virt_addr: int
	dlen:      int
	daddr:     int
	flags:     int
	
	_fields_ = [
		('naddr', c_int32),
		('nlen', c_int32),
		('phys_addr', c_int32),
		('virt_addr', c_int32),
		('dlen', c_int32),
		('daddr', c_int32),
		('rsvd', (c_char * 16)),
		('flags', c_int32),
		('rsvd2', (c_char * 4))
	]

def get_name(dview: memoryview, naddr: int, nlen: int) -> str:
	return dview[naddr:naddr+nlen].tobytes().decode()