import os
import random
from pathlib import Path

path = Path("Backgroundimages")
files = os.listdir(path)
index = random.randrange(0, len(files))
print(files[index])
