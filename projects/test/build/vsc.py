import targets
from ctms.ucbuild import vsc
from settings import ProjDirs

# Generate visual studio code c properties file
print(f"Generating {vsc.CPROPS_FNAME}...")
vsc.generate_cprops(ProjDirs.vsc, targets.all.values())