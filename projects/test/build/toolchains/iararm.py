import os
import settings
from ctms.ucbuild import ToolchainId, BuildTarget
from pathlib import Path

# Input & output file keys
LSCR_KEY = "lscr"
ELF_KEY  = "elf"
MAP_KEY  = "map"

# General settings
tool_ver = "9.60.3"

def get_toolchain_id() -> ToolchainId:
	return ToolchainId.iararm

def get_tool_dir() -> Path:
	return Path(os.environ["IAR_ROOT"], f"ewarm-{tool_ver}", "arm/bin")

def get_c_std() -> str:
	return "c23"

def get_i_mode() -> str:
	return "clang"
	
def get_sys_cc_incs() -> list[Path]:
	return []
	
def get_sys_cc_defs() -> list[str]:
	return []
	
def configure(target: BuildTarget):
	target.add_cc_opts([])
	target.add_cc_incs([settings.src_dir])
	target.add_cc_defs([])
	target.add_cc_output("-lA {}", ".lst")
	target.add_ld_lib_dirs([])
	target.add_ld_libs([])
	
def add_lscript_input(target: BuildTarget):
	target.add_ld_input(
		LSCR_KEY, "--config {}",
		Path(settings.link_dir, f"{target.name}.icf"))
	
def add_elf_output(fname: str, target: BuildTarget):
	target.add_ld_output(
		ELF_KEY, "-o {}",
		Path(target.out_dir, f"{fname}.out"))
	
def add_map_output(fname: str, target: BuildTarget):
	target.add_ld_output(
		MAP_KEY, "--map {}",
		Path(target.out_dir, f"{fname}.map"))
	
def add_sources(target: BuildTarget):
	target.add_sources(settings.src_dir, recurse = True)
	target.rem_sources(settings.targ_srcd, recurse = True)
	target.add_sources(Path(settings.src_dir, target.name), recurse = True)