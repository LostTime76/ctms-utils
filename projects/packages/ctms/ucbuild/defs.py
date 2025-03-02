from dataclasses import dataclass
from enum import Enum, StrEnum
from pathlib import Path

class BuildMode(StrEnum):
	""" Represents the type of a build """

	debug = "debug",
	""" Unoptimized build containing debugging information for development """

	release = "release"
	""" Optimized build intended for release """

class Toolchain(Enum):
	""" Describes the toolchain used for the build """

	iararm = "iararm"
	""" iar arm toolchain """

class CStandard(Enum):
	""" Describes the c standard being used for the build """

	c17 = "c17"
	""" The c17 standard """

	c23 = "c23"
	""" The c23 standard """

class CppStandard(Enum):
	""" Describes the c++ standard being used for the build """

	cpp98 = "c++98"
	""" The c++ 98 standard """

@dataclass
class CompilerFileSpec:
	""" Contains the properties to describe an output file for the compiler """

	fmt: str
	""" Gets the command line invocation format for the file """

	fext: str
	""" Gets the extension of the file """

@dataclass
class LinkerFileSpec:
	""" Contains the properties to describe an input or output file for the linker """

	fmt: str
	""" Gets the command line invocation format for the file """

	fpath: Path
	""" Gets the path of the file """

class VscIntellisenseMode(Enum):
	""" Describes the intellisense mode for c/c++ projects within visual studio code"""

	clang_arm = "clang-arm"
	""" Clang arm intellisense mode """