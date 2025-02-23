import sys

if (len(sys.argv) < 2):
	raise Exception("Expected a command!")
match (cmd := sys.argv[1].lower()):
	case "clean":
		from .commands import clean
	case _:
		raise Exception(f"Unrecognized command: '{cmd}' !")