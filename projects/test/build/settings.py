from pathlib import Path

# General settings
threads  = 1
base_scn = "31634"

# Project directories
bld_dir  = Path(__file__).parent
proj_dir = bld_dir.parent
link_dir = Path(bld_dir, "linker")
artf_dir = Path(proj_dir, "artifacts")
vsc_dir  = Path(proj_dir, ".vscode")

# Source directories
src_dir   = Path(proj_dir, "src")
targ_srcd = Path(src_dir, "targets")
lots_srcd = Path(src_dir, "lots")

def get_threads() -> int:
	return threads
	
def get_artifacts_dir() -> Path:
	return artf_dir
	
def get_vsc_dir() -> Path:
	return vsc_dir