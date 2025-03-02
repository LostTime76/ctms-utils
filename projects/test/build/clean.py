import shutil
from settings import ProjDirs

# Clean artifacts
print("Cleaning artifacts...")
shutil.rmtree(ProjDirs.artifacts, True)

# Generate vsc properties
import vsc