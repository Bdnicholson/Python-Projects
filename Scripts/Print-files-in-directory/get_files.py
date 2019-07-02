import os
import glob


# replace path in quotes with desired path
os.chdir("/Users/bonicholson/Projects/Python-Projects/Grade-Average")
# replace .py with the extension you desire
for file in glob.glob("*.py"):
    print(file)