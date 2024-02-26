#!/usr/bin/env python3

from os import chdir, path, system
from sys import stdout
from yaml import safe_load

files = safe_load (open('files.yaml', 'r'))
files.append({'folder': 'Relex12.github.io'})

chdir("..")

for i in range(len(files)):
    folder = files[i]["folder"]
    if (not path.exists(f"{folder}/")):
        stdout.write(f"\rCoping {folder}..."+30*' ')
        system(f"git clone --quiet https://github.com/Relex12/{folder}.git")
stdout.write("\n")
