from ctypes import *
from pathlib import Path

# Load the library
_lib = CDLL(Path(Path(__file__).parent, 'clib.dll'))

# Load the library functions
free_mem    = CFUNCTYPE(None, c_void_p)(('free_mem', _lib))
_get_errmsg = CFUNCTYPE(c_void_p)(('get_errmsg', _lib))

# Load the bit operations
rev16 = CFUNCTYPE(None, c_char_p, c_int32)(('rev16', _lib))
crc32 = CFUNCTYPE(c_int32, c_char_p, c_int32)(('crc32', _lib))

# Load the coff functions
coff_load       = CFUNCTYPE(c_bool, c_char_p, c_int32, c_void_p)(('coff_load', _lib))
coff_sects      = CFUNCTYPE(c_bool, c_void_p, c_void_p)(('coff_sects', _lib))
coff_copy_sects = CFUNCTYPE(None, c_int32, c_int32, c_char_p, c_char_p,	c_void_p, c_int32)(('coff_copy_sects', _lib))

def to_ptr(data: bytes | bytearray) -> c_char_p:
	return data if data is isinstance(data, bytes) else (c_char * len(data)).from_buffer(data)

def error():
	if (msgp := _get_errmsg()) is None:
		return
	msg = cast(msgp, c_char_p).value.decode()
	free_mem(msgp)
	raise Exception(msg)