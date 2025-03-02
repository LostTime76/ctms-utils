import sys
import targets
from argparse import ArgumentParser
from dataclasses import dataclass
from targets.iararm import IarArmTarget

@dataclass
class Options:
	target: str

# Create a new parser
parser = ArgumentParser(prog = "Project build command")

# The target option is required
parser.add_argument("target", choices = targets.all.keys())

# Parse the args
args: Options = parser.parse_args(sys.argv[1:])

# Get the target
target: IarArmTarget = targets.all[args.target]


stree = target.sources

s = stree.sources()

print()