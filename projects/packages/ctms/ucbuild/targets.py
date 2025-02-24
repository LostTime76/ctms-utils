from . import settings
from enum import Enum
from types import ModuleType
from typing import Protocol

class ToolchainId(Enum):
	iararm = "iararm"

class BuildTargetSpec(Protocol):

	def get_toolchain_id(self) -> ToolchainId: ...

	@staticmethod
	def is_spec(module: ModuleType) -> bool:
		return hasattr(module, BuildTargetSpec.get_toolchain_id.__name__)

class BuildTarget:

	_name : str
	_spec : BuildTargetSpec

	def __init__(self, name: str, spec: BuildTargetSpec):
		self._spec = spec

	@staticmethod
	def _from_spec(spec: BuildTargetSpec) -> BuildTarget:
		pass

	@staticmethod
	def _from_mname(mname: str) -> BuildTarget | None:



		pass