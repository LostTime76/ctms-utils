from ctms.ucbuild import SourceTree
from pathlib import Path
from typing import Protocol

class IBuildConfig(Protocol):

	@property
	def name(self) -> str:
		...

	@property
	def out_dir(self) -> Path:
		...

	@property
	def c_opts(self) -> list[str | Path]:
		...

	@property
	def c_incs(self) -> list[str | Path]:
		...

	@property
	def c_defs(self) -> list[str | Path]:
		...

	@property
	def sources(self) -> SourceTree:
		...