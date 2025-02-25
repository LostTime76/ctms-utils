from pathlib import Path

class ProjDirs:
	build     = Path(__file__).parent
	root      = build.parent
	linker    = Path(build, "linker")
	targets   = Path(build, "targets")
	artifacts = Path(root, "artifacts")
	vsc       = Path(root, ".vscode")

class SrcDirs:
	root    = Path(ProjDirs.root, "src")
	lots    = Path(root, "lots")
	targets = Path(root, "targets")