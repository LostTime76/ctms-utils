from abc import ABC, abstractmethod
from ctms.ucbuild.sources import SourceTree
from pathlib import Path

from ctms.ucbuild.defs import (
	BuildMode,
	Toolchain,
	CStandard,
	CppStandard,
	CompilerFileSpec,
	LinkerFileSpec,
	VscIntellisenseMode
)

class BuildTarget(ABC):

	_key      : str
	_mode     : BuildMode
	_out_dir  : Path
	_cc_opts  : list[str] | None
	_cc_incs  : list[Path] | None
	_cc_defs  : list[str] | None
	_cc_outs  : list[CompilerFileSpec]
	_ld_opts  : list[str] | None
	_ld_ldirs : list[Path] | None
	_ld_libs  : list[Path] | None
	_ld_ins   : dict[str, LinkerFileSpec] | None
	_ld_outs  : dict[str, LinkerFileSpec] | None
	_sources  : SourceTree | None
	
	def __init__(self, mode: BuildMode):
		self._key      = f"{self.name}.{mode.name}"
		self._mode     = mode
		self._out_dir  = Path(self.artf_dir if self.artf_dir else Path.cwd(), self.key)
		self._cc_opts  = None
		self._cc_incs  = None
		self._cc_defs  = None
		self._cc_outs  = None
		self._ld_opts  = None
		self._ld_ldirs = None
		self._ld_libs  = None
		self._ld_ins   = None
		self._ld_outs  = None
		self._sources  = None

	def _init_cc_opts(self): ...
	def _init_cc_incs(self): ...
	def _init_cc_defs(self): ...
	def _init_cc_outputs(self): ...
	def _init_ld_opts(self): ...
	def _init_ld_ldirs(self): ...
	def _init_ld_libs(self): ...
	def _init_ld_inputs(self): ...
	def _init_ld_outputs(self): ...
	def _init_sources(self): ...

	@staticmethod
	def create_all(types: list[type]) -> dict[str, BuildTarget]:
		targets = dict()
		for type in types:
			for mode in BuildMode:
				target: BuildTarget = type(mode)
				targets[target.key] = target
		return targets
	
	@property
	@abstractmethod
	def name(self) -> str: ...
	
	@property
	@abstractmethod
	def toolchain(self) -> Toolchain: ...

	@property
	@abstractmethod
	def tool_dir(self) -> Path: ...

	@property
	def src_dir(self) -> Path | None:
		return None

	@property
	def artf_dir(self) -> Path | None:
		return None
	
	@property
	def key(self) -> str:
		return self._key
	
	@property
	def mode(self) -> BuildMode:
		return self._mode
	
	@property
	def out_dir(self) -> Path:
		return self._out_dir
	
	@property
	def cc_opts(self) -> list[str]:
		if self._cc_opts is None:
			self._cc_opts = []
			self._init_cc_opts()
		return self._cc_opts
	
	@property
	def cc_incs(self) -> list[Path]:
		if self._cc_incs is None:
			self._cc_incs = []
			self._init_cc_incs()
		return self._cc_incs
	
	@property
	def cc_defs(self) -> list[str]:
		if self._cc_defs is None:
			self._cc_defs = []
			self._init_cc_defs()
		return self._cc_defs
	
	@property
	def cc_outputs(self) -> list[CompilerFileSpec]:
		if self._cc_outs is None:
			self._cc_outs = []
			self._init_cc_outputs()
		return self._cc_outs
	
	@property
	def ld_opts(self) -> list[str]:
		if self._ld_opts is None:
			self._ld_opts = []
			self._init_ld_opts()
		return self._ld_opts
	
	@property
	def ld_ldirs(self) -> list[Path]:
		if self._ld_ldirs is None:
			self._ld_ldirs = []
			self._init_ld_ldirs()
		return self._ld_ldirs
	
	@property
	def ld_libs(self) -> list[Path]:
		if self._ld_libs is None:
			self._ld_libs = []
			self._init_ld_libs()
		return self._ld_libs
	
	@property
	def ld_inputs(self) -> dict[str, LinkerFileSpec]:
		if self._ld_ins is None:
			self._ld_ins = dict()
			self._init_ld_inputs()
		return self._ld_ins
	
	@property
	def ld_outputs(self) -> dict[str, LinkerFileSpec]:
		if self._ld_outs is None:
			self._ld_outs = dict()
			self._init_ld_outputs()
		return self._ld_outs
	
	@property
	def sources(self) -> SourceTree:
		if self._sources is None:
			self._sources = SourceTree(self.src_dir, self.as_fexts, self.c_fexts, self.cpp_fexts)
			self._init_sources()
		return self._sources
	
	@property
	def c_std(self) -> CStandard | None:
		return None
	
	@property
	def cpp_std(self) -> CppStandard | None:
		return None
	
	@property
	def as_fexts(self) -> set[str]:
		return { ".s" }
	
	@property
	def c_fexts(self) -> set[str]:
		return { ".c" }
	
	@property
	def cpp_fexts(self) -> set[str] | None:
		return None
	
	@property
	def vsc_i_mode(self) -> VscIntellisenseMode | None:
		return None
	
	@property
	def vsc_cc_incs(self) -> list[Path]:
		return []
	
	@property
	def vsc_cc_defs(self) -> list[str]:
		return []