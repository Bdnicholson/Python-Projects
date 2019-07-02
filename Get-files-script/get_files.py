import os
import glob

# Change path to the folder you want to search

os.chdir("/Users/bonicholson/Projects....")

# change .xxx to desired file extension
for file in glob.glob("*.xxxx"):
    print(file)
    