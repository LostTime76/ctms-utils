from pathlib import Path
from typing import Protocol

class BuildSettingsSpec(Protocol):
	
	@staticmethod
	def get_threads() -> int: ...

	@staticmethod
	def get_artifacts_dir() -> Path: ...

	@staticmethod
	def get_vsc_dir() -> Path: ...