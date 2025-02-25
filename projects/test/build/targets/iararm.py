from ctms.ucbuild import Toolchain, BuildTarget
from pathlib import Path
from settings import ProjDirs, SrcDirs

class IarArmTarget(BuildTarget):
	
	LSCR_KEY = "lscr"
	ELF_KEY  = "elf"
	MAP_KEY  = "map"
	
	def __init__(self):
		super().__init__(Toolchain.iararm, Path(ProjDirs.artifacts, self.name))
		
	def add_lscript(self, fpath: Path):
		self.add_ld_input(self.LSCR_KEY, "--config {}", fpath)
		
	def add_elf(self, fname: str):
		self.add_ld_output(self.ELF_KEY, "-o {}", Path(self.out_dir, f"{fname}.out"))
		
	def add_map(self, fname: str):
		self.add_ld_output(self.MAP_KEY, "--map {}", Path(self.out_dir, f"{fname}.map"))
		
	def add_cc_incs_core(self):
		self.add_cc_incs([SrcDirs.root])
		
	def add_sources_core(self):
		self.add_sources(SrcDirs.root)
		self.rem_sources(SrcDirs.targets)
		self.add_sources(Path(SrcDirs.targets, self.name))
		
	@property
	def c_std(self) -> str: return "c23"
		
	@property
	def i_mode(self) -> str: return "clang"
	
	@property
	def lscript_fpath(self) -> Path: return self.get_ld_input(self.LSCR_KEY)
	
	@property
	def elf_fpath(self) -> Path: return self.get_ld_output(self.ELF_KEY)
	
	@property
	def map_fpath(self) -> Path: return self.get_ld_output(self.MAP_KEY)