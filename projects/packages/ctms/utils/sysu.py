import sys

def strip_argv(start: int = 1, count: int = 1):
	"""
	Strips (removes) a number of arguments from within the system command line argument array

	Parameters
	----------
	start
		The index of the starting argument within the array to strip
	count
		The number of arguments to strip from the array
	"""
	del sys.argv[start:start+count]

def exit(msg: str | None = None, code: int = 0):
	"""
	Prints an optional message to the standard output and exits the program

	Parameters
	----------
	msg
		The optional message to print to the standard output. If the msg is None, no message is
		printed to the standard output
	code
		The process exit code
	"""

	if msg is not None:
		print(msg)
	sys.exit(code)