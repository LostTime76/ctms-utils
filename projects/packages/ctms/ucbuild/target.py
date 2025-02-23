from enum import Enum
from pathlib import Path
from typing import Protocol

class ToolchainId(Enum):
	iararm = "iar-arm"

class ToolchainSpec(Protocol):
	pass

class BuildTargetSpec(Protocol):
	pass

class BuildTarget:

	def add_cc_opts(self, opts: list[str]):
		pass

	def add_cc_incs(self, incs: list[Path]):
		pass

	def add_cc_defs(self, defs: list[str]):
		pass

	def add_cc_output(self, fmt: str, fext: str):
		pass

	def add_ld_lib_dirs(self, dirs: list[Path]):
		pass

	def add_ld_libs(self, libs: list[Path]):
		pass

	def add_ld_input(self, key: str, fmt: str, fpath: Path):
		pass

	def add_ld_output(self, key: str, fmt: str, fpath: Path):
		pass

	def add_output(self, key: str, fpath: Path):
		pass

	def add_sources(self, dir: Path, files: list[str] | None = None, recurse: bool = False):
		pass

	def rem_sources(self, dir: Path, files: list[str] | None = None, recurse: bool = False):
		pass
	
	@property
	def name(self) -> str:
		pass

	@property
	def out_dir(self) -> Path:
		pass