import importlib
from .interface import IBuildConfig

_names = {
	"debug",
	"release"
}

def get(name: str) -> IBuildConfig:
	name = name.lower()
	if name not in _names:
		raise Exception(f"\"{name}\" is not a valid build config!")
	return importlib.import_module(f"{__name__}.{name}")

def all() -> list[IBuildConfig]:
	return [get(name) for name in _names]