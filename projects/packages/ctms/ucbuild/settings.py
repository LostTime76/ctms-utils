from . import specu
from ctms.utils import impu
from pathlib import Path
from typing import Protocol

class BuildSettingsSpec(Protocol):

	def get_thread_count(self) -> int: ...

	def get_artifacts_dir(self) -> Path: ...

	def get_vsc_dir(self) -> Path: ...

class BuildSettings:

	# Constants
	TARGETS    = "targets"
	TOOLCHAINS = "toolchains"
	SETTINGS   = "settings"
	VSC_PROPS  = "c_cpp_properties.json"

	# Static variables
	_inst : BuildSettings = None

	# Instance variables
	_threads    : int
	_proj_dir   : Path
	_targs_dir  : Path
	_toolcs_dir : Path
	_artf_dir   : Path
	_vscp_fpath : Path

	def __init__(self, spec: BuildSettingsSpec):
		self._proj_dir   = Path.cwd()
		self._targs_dir  = Path(self._proj_dir, self.TARGETS)
		self._toolcs_dir = Path(self._proj_dir, self.TOOLCHAINS)
		self._threads    = specu.get_int(spec, BuildSettingsSpec.get_thread_count)
		self._artf_dir   = self._get_artf_dir(spec)
		self._vscp_fpath = self._get_vscp_fpath(spec)

	@staticmethod
	def _get_artf_dir(spec: BuildSettingsSpec):
		if (dir := specu.get_dir(spec, BuildSettingsSpec.get_artifacts_dir)) is None:
			raise Exception("The artifacts directory must be defined within the settings.")
		return dir

	@staticmethod
	def _get_vscp_fpath(spec: BuildSettingsSpec) -> Path | None:
		if (dir := specu.get_dir(spec, BuildSettingsSpec.get_vsc_dir)) is None:
			return None
		return Path(dir, BuildSettings.VSC_PROPS)

	@staticmethod
	def _load() -> BuildSettings:
		if ((spec := impu.try_import(BuildSettings.SETTINGS)) is None):
			raise Exception("Could not load settings module.")
		return BuildSettings(spec)

	@staticmethod
	def get_instance() -> BuildSettings:
		if BuildSettings._inst is None:
			BuildSettings._inst = BuildSettings._load()
		return BuildSettings._inst

	@property
	def threads(self) -> int:
		return self._threads

	@property
	def proj_dir(self) -> Path:
		return self._proj_dir

	@property
	def targets_dir(self) -> Path:
		return self._targs_dir

	@property
	def toolcs_dir(self) -> Path:
		return self._toolcs_dir

	@property
	def artf_dir(self) -> Path:
		return self._artf_dir

	@property
	def vscp_fpath(self) -> Path | None:
		return self._vscp_fpath