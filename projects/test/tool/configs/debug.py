import settings
from pathlib import Path

# General settings
name    = __name__
out_dir = Path(settings.artf_dir, name)

# C compiler options
c_opts = settings.c_opts + []

# C compiler includes
c_incs = settings.c_incs + []

# C compiler defines
c_defs = settings.c_opts + ["DEBUG"]

# Source files
sources = settings.sources

# Add all of the files within the debug config source directory
sources.add(Path(settings.src_config_dir, name))