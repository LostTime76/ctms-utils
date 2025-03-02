from pathlib import Path

class ProjDirs:
	""" Static class containing all of the project related directories """

	build = Path(__file__).parent
	""" Gets the path to this build directory """

	root = build.parent
	""" Gets the path to the c project directory """

	lscript = Path(build, "lscript")
	""" Gets the path to the linker script directory """

	artifacts = Path(root, "artifacts")
	""" Gets the path to the c project artifacts directory """

	vsc = Path(root, ".vscode")
	""" Gets the path to the c project visual studio code directory """

class SrcDirs:
	""" Static class containing all of the c project source file related directories """

	root = Path(ProjDirs.root, "src")
	""" Gets the path to the root source directory """

	lots = Path(root, "lots")
	""" Gets the path to the lots source directory """

	targets = Path(root, "targets")
	""" Gets the path to the targets source directory """