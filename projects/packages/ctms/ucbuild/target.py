import inspect
from abc import ABC, abstractmethod
from ctms.utils import impu
from enum import Enum
from pathlib import Path
from types import ModuleType

class Toolchain(Enum):
	iararm = "iararm"

class BuildTarget(ABC):

	def __init__(self, toolchain: Toolchain, out_dir: Path):
		pass

	def add_cc_incs(self, incs: list[Path]):
		pass

	def add_ld_input(self, key: str, format: str, fpath: Path):
		pass

	def add_ld_output(self, key:str, format: str, fpath: Path):
		pass

	def add_sources(self, dir: Path, files: list[str] | None = None, recurse: bool = True):
		pass

	def rem_sources(self, dir: Path, files: list[str] | None = None, recurse: bool = True):
		pass

	def get_ld_input(self, key: str) -> Path:
		pass

	def get_ld_output(self, key: str) -> Path:
		pass

	@staticmethod
	def from_file(package: str | None, fpath: Path) -> BuildTarget | None:
		fname = fpath.stem
		mname = f"{package}.{fname}" if package is not None else fname
		if (module := impu.try_import(mname)) is None:
			return None
		elif (type := BuildTarget._get_target_type(module)) is None:
			return None
		return type()
	
	@staticmethod
	def all_from_dir(dir: Path, package: str | None) -> dict[str, BuildTarget]:
		targets = dict()
		for fpath in dir.iterdir():
			if not fpath.is_file():
				continue
			elif (target := BuildTarget.from_file(package, fpath)) is None:
				continue
			targets[target.name] = target
		return targets
		
	@staticmethod
	def _get_target_type(module: ModuleType) -> type | None:
		types = inspect.getmembers(module, predicate = BuildTarget._is_target_type)
		return types[0][1] if len(types) > 0 else None

	@staticmethod
	def _is_target_type(obj: any) -> bool:
		return inspect.isclass(obj) and issubclass(obj, BuildTarget) and \
			not inspect.isabstract(obj)

	@property
	@abstractmethod
	def name(self) -> str: ...

	@property
	def out_dir(self) -> Path: ...