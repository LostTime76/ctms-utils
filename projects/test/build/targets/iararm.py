import os
from pathlib import Path
from settings import ProjDirs, SrcDirs

from ctms.ucbuild import (
	Toolchain,
	BuildMode,
	BuildTarget,
	CStandard,
	CompilerFileSpec,
	LinkerFileSpec,
	VscIntellisenseMode
)

class IarArmTarget(BuildTarget):

	TOOL_VER  = "9.60.3"
	TOOL_ROOT = Path(os.environ["IAR_ROOT"], f"ewarm-{TOOL_VER}/arm")
	LSCR_KEY  = "lscr"
	ELF_KEY   = "elf"
	MAP_KEY   = "map"
	
	def __init__(self, mode: BuildMode):
		super().__init__(mode)

	def _init_cc_opts(self):
		self.cc_opts.append(f"-O{"hz" if self.mode == BuildMode.release else "n"}")

	def _init_cc_incs(self):
		self.cc_incs.append(SrcDirs.root)

	def _init_cc_defs(self):
		self.cc_defs.append(self.mode.name.upper())

	def _init_cc_outputs(self):
		self.cc_outputs.append(self._get_lst_fspec())

	def _init_ld_inputs(self):
		self.ld_inputs[self.LSCR_KEY] = self._get_lscript_fspec()

	def _init_ld_outputs(self):
		self.ld_outputs[self.ELF_KEY] = self._get_elf_fspec()
		self.ld_outputs[self.MAP_KEY] = self._get_map_fspec()

	def _init_sources(self):
		self.sources.r_inc(SrcDirs.root)
		self.sources.r_inc(SrcDirs.targets, False)
		self.sources.r_inc(Path(SrcDirs.targets, self.name))

	def _get_lst_fspec(self) -> CompilerFileSpec:
		return CompilerFileSpec("-lA {}", ".lst")
	
	def _get_lscript_fspec(self) -> LinkerFileSpec:
		return LinkerFileSpec("--config {}", Path(ProjDirs.lscript, f"{self.key}.icf"))
	
	def _get_elf_fspec(self) -> LinkerFileSpec:
		return LinkerFileSpec("-o {}", Path(self.out_dir, f"{self.name}.out"))
	
	def _get_map_fspec(self) -> LinkerFileSpec:
		return LinkerFileSpec("--map {}", Path(self.out_dir, f"{self.name}.map"))
		
	@property
	def toolchain(self) -> Toolchain:
		return Toolchain.iararm
	
	@property
	def tool_dir(self) -> Path:
		return Path(self.TOOL_ROOT, "bin")
	
	@property
	def artf_dir(self) -> Path:
		return ProjDirs.artifacts
	
	@property
	def src_dir(self) -> Path:
		return SrcDirs.root
		
	@property
	def c_std(self) -> CStandard:
		return CStandard.c23
	
	@property
	def vsc_i_mode(self) -> str:
		return VscIntellisenseMode.clang_arm
	
	@property
	def vsc_cc_incs(self) -> list[Path]:
		return [Path(self.TOOL_ROOT, "inc/c")]
	
	@property
	def lscript_fpath(self) -> Path:
		return self.ld_inputs[self.LSCR_KEY]
	
	@property
	def elf_fpath(self) -> Path:
		return self.ld_outputs[self.ELF_KEY]
	
	@property
	def map_fpath(self) -> Path:
		return self.ld_outputs[self.MAP_KEY]