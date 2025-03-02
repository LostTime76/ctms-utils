from ctms.ucbuild import BuildMode
from targets.iararm import IarArmTarget

class UltraTarget(IarArmTarget):
	
	def __init__(self, mode: BuildMode):
		super().__init__(mode)

	@property
	def name(self) -> str:
		return "ultra"