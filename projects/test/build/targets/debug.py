import toolchains.iararm as iararm
from ctms.ucbuild import ToolchainId

def get_toolchain_id() -> ToolchainId:
	return ToolchainId.iararm