from pathlib import Path

class ProjDirs:
	build     = Path(__file__).parent
	root      = build.parent
	targets   = Path(build, "targets")
	artifacts = Path(root, "artifacts")
	vsc       = Path(root, ".vscode")

class SrcDirs:
	root    = Path(ProjDirs.root, "src")
	lots    = Path(root, "lots")
	targets = Path(root, "targets")

def get_thread_count() -> int:
	return 1
	
def get_artifacts_dir() -> Path:
	return ProjDirs.artifacts
	
def get_vsc_dir() -> Path:
	return ProjDirs.vsc