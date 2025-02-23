import shutil
from ..settings import BuildSettings
from ctms.utils import sysu

# Strip args
sysu.strip_argv()

# Get the build settings
settings = BuildSettings.get_inst()

# Make sure there is something to clean
if (settings.artf_dir is None):
	sysu.exit("Nothing to clean")

# Clean artifacts
print("Cleaning artifacts...")
shutil.rmtree(settings.artf_dir, True)