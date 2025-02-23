import utils
import toolchains.iararm as iararm
from ctms.ucbuild import ToolchainSpec, BuildTarget, MicroBuild

_scn = utils.get_scn("TST, CAN")

def get_toolchain_spec() -> ToolchainSpec:
	return iararm
	
def configure(target: BuildTarget):
	iararm.configure(target)
	iararm.add_lscript_input(target)
	iararm.add_elf_output(_scn, target)
	iararm.add_map_output(_scn, target)
	target.add_cc_opts([])
	target.add_cc_incs([])
	target.add_cc_defs([])
	
def add_sources(target: BuildTarget):
	iararm.add_sources(target)
	
def after_build(build: MicroBuild):
	pass