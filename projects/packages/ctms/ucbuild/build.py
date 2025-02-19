from pathlib import Path
from .rules import CompileRule

class SourceTree:

	def __init__(self, root: str | Path):
		pass

	def add(self,
		dir: str | Path | None = None,
		files: list[str | Path] | None = None,
		recurse: bool = False):
		pass

	def rem(self,
		dir: str | Path | None = None,
		files: list[str | Path] | None = None,
		recurse: bool = False):
		pass

class MicroBuild:

	def __init__(self,
		threads: int = 1,
		out_dir: str | Path | None = None,
		c_rule: CompileRule | None = None,
		sources: SourceTree | None = None):
		pass