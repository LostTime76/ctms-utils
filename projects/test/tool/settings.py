import os
from ctms.ucbuild import rules, CompileRule, SourceTree
from pathlib import Path

# Directories
tool_dir = Path(__file__).parent
proj_dir = Path(tool_dir).parent
artf_dir = Path(proj_dir, "artifacts")

# Source directories
src_dir        = Path(proj_dir, "src")
src_config_dir = Path(src_dir, "config")

# C compiler settings
c_exe  = "clang"
c_rsp  = (rules.rsp_fmt, rules.rsp_fext)
c_spec = ""

# Default C compiler options
c_opts = ["-c"]

# Default C compiler includes
c_incs = [src_dir]

# Default C compiler defines
c_defs = []

# Default sources
sources = SourceTree(src_dir)

# Adds all sources within the tree
sources.add()

# Remove sources within the config source directory, individual build configs will add their
# respective files
sources.rem(dir = src_config_dir, recurse = True)