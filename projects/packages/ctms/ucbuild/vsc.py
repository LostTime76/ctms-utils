from ctms.ucbuild.target import BuildTarget
from ctms.utils import jsonu
from pathlib import Path
from typing import Iterable

CPROPS_FNAME = "c_cpp_properties.json"
""" Gets the name of the c properties file """

def generate_cprops(vsc_dir: Path, targets: Iterable[BuildTarget]):
	jsonu.fwrite(Path(vsc_dir, CPROPS_FNAME), _get_json(targets))

def _get_json(targets: Iterable[BuildTarget]) -> dict[str, any]:
	return { 
		"version": 4,
		"configurations": [_get_target_json(target) for target in targets]
	}

def _get_target_json(target: BuildTarget):

	# Create basic config
	json = {
		"name": target.key,
		"includePath": _get_paths(target.vsc_cc_incs + target.cc_incs),
		"defines": target.vsc_cc_defs + target.cc_defs
	}

	# Add additional properties that may not be set
	return _add_maybe_nones(json, target)

def _add_maybe_nones(json: dict[str, any], target: BuildTarget) -> dict[str, any]:
	if target.c_std is not None:
		json["cStandard"] = target.c_std.value
	if target.cpp_std is not None:
		json["cppStandard"] = target.cpp_std.value
	if target.vsc_i_mode is not None:
		json["intelliSenseMode"] = target.vsc_i_mode.value
	return json

def _get_paths(paths: list[Path]):
	return [str(path.resolve()) for path in paths]