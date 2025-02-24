from pathlib import Path
from typing import Callable

def get_int(obj: any, func: Callable) -> int:
	aname = func.__name__
	if not hasattr(obj, aname):
		return 0
	value = getattr(obj, aname)()
	return value if isinstance(value, int) else 0

def get_dir(obj: any, func: Callable) -> Path | None:
	aname = func.__name__
	if not hasattr(obj, aname):
		return None
	dir = getattr(obj, aname)()
	return dir if isinstance(dir, Path) else None