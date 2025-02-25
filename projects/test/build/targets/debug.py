from pathlib import Path
from settings import ProjDirs
from targets.iararm import IarArmTarget

class DebugTarget(IarArmTarget):
	
	def __init__(self):
		super().__init__()
		
	def add_ld_inputs_core(self):
		self.add_lscript(Path(ProjDirs.linker, self.name))
		
	def add_ld_outputs_core(self):
		self.add_elf(self.name)
		self.add_map(self.name)
		
	def add_sources_core(self):
		super().add_sources_core()
		
	@property
	def name(self) -> str: return "debug"