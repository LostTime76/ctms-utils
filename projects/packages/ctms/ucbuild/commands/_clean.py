import importlib, shutil
from ..targets import BuildTargetSpec, BuildTarget
from ..settings import BuildSettings
from ctms.utils import jsonu
from pathlib import Path

def exec():

	# Get settings
	settings = BuildSettings.get_instance()

	# Clean artifacts
	print("Cleaning artifacts...")
	shutil.rmtree(settings.artf_dir, True)

	# Check if we are generating VSC properties
	if (vscp_fpath := settings.vscp_fpath) is None:
		return

	# Get all of the build targets
	targets = _get_targets(settings)

	# Generate VSC properties
	print(f"Generating {BuildSettings.VSC_PROPS}...")
	jsonu.fwrite(vscp_fpath, _get_vscp_json(targets))

def _get_vscp_json(targets: list[BuildTarget]):
	return { "configurations": [_get_target_json(target) for target in targets] }

def _get_target_json(target: BuildTarget):
	return None

def _get_targets(settings: BuildSettings) -> list[BuildTarget]:
	targets = []
	for fpath in settings.target_dir.iterdir():
		if not fpath.is_file():
			continue
		module = importlib.import_module(f"{BuildSettings.TARGETS}.{fpath.stem}")
		if not BuildTargetSpec.is_spec(module):
			continue
		targets.append(BuildTarget(module))
	return targets