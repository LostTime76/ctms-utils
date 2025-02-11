import json
from pathlib import Path
from . import fileu

def fwrite(fpath: Path, object: any, neq: bool = True):
	"""
	Serializes an object to json and writes it to a file. Any intermediate directories are created
	if they do not already exist.
	
	Parameters
	----------
	fpath
		The path to the json file to write
	object
		The object to serialize into json
	neq
		Set to True to create the file only if the contents of any existing file do not match the
		text to be written. Otherwise, the file is always created.
	"""
	fileu.write_text(fpath, json.dumps(object, indent = "\t", separators = (',', ': ')), neq)
