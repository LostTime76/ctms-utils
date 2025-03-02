from ctms.ucbuild import BuildTarget
from targets.ultra import UltraTarget

all = BuildTarget.create_all([UltraTarget])
""" Gets all of the targets available within the project"""