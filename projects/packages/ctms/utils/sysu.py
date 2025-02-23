import sys

def strip_argv():
	sys.argv[1:] = sys.argv[len(sys.argv):]

def exit(msg: str | None = None, code: int = 0):
	if msg is not None:
		print(msg)
	sys.exit(code)