import importlib
from types import ModuleType

def try_import(mname: str) -> ModuleType | None:
	"""
	Tries to import a module within the current program context with the given name

	Parameters
	----------
	mname
		The name of the module to import

	Returns
	-------
	The module if it was imported successfully, otherwise None
	"""
	try:
		return importlib.import_module(mname)
	except:
		return None