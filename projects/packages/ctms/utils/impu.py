import importlib
from types import ModuleType

def try_import(mname: str) -> ModuleType | None:
	try:
		return importlib.import_module(mname)
	except:
		return None