#!/usr/bin/env python3

from os import chdir, path, system
from yaml import safe_load

files = safe_load (open('files.yaml', 'r'))

chdir("..")

for i in range(len(files)):
    folder = files[i]["folder"]
    if (not path.exists("{}/".format(folder))):
        system("git clone https://github.com/Relex12/{}.git".format(folder))
