from pathlib import Path

def write_text(fpath: Path, text: str, neq: bool = True):
	"""
	Creates a new file and writes text to it. Any intermediate directories are created if they do
	not already exist.

	Parameters
	----------
	fpath
		The path to the file to write
	text
		The text to write to the file
	neq
		Set to True to create the file only if the contents of any existing file do not match the
		text to be written. Otherwise, the file is always created.
	"""
	if (not neq) or (not fpath.exists()) or (fpath.read_text() != text):
		fpath.parent.mkdir(parents = True, exist_ok = True)
		fpath.write_text(text)