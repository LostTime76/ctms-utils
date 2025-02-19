from pathlib import Path
from typing import Self

rsp_fmt   = "@{}"
rsp_fext  = ".rsp"
obj_fext  = ".o"
deps_fext = ".d"

class CompileRule:

	def __init__(self,
		exe: str | Path,
		rsp: tuple[str, str] | None = None,
		opts: list[str | Path] | None = None,
		incs: list[str | Path] | None = None,
		defs: list[str | Path] | None = None):
		pass