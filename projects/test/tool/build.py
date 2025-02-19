import configs, settings, sys
from ctms.ucbuild import CompileRule, MicroBuild

# Get the selected build config
config = configs.get(sys.argv[1])

# C compile rule
c_rule = CompileRule(
	exe  = settings.c_exe,
	rsp  = settings.c_rsp,
	opts = config.c_opts,
	incs = config.c_incs,
	defs = config.c_defs
)

# Create a new build
build = MicroBuild(
	out_dir = config.out_dir,
	c_rule  = c_rule,
	sources = config.sources
)