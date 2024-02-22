#!/usr/bin/env python3

from os import path
from os import system
from yaml import safe_load

if (not path.exists("../Relex12.github.io/")):
    raise FileNotFoundError("Relex12.github.io directory not found")
if (not path.exists("../Markdown-Table-of-Contents/")):
    raise FileNotFoundError("Markdown-Table-of-Contents directory not found")

#####################
# FILES DECLARATION #
#####################

files = safe_load (open('files.yaml', 'r'))


####################
# FILES GENERATION #
####################

for i in range(len(files)):
    if (path.exists("../{}/".format(files[i]["folder"]))):
        system("python3 ../Markdown-Table-of-Contents/toc.py ../{}/{}".format(files[i]["folder"], files[i]["file"]))
        input_file = open("../{}/{}".format(files[i]["folder"], files[i]["file"]), 'r')
        front_matter = """---
layout: {}
title: "{}"
permalink: {}
---

""".format(files[i]["layout"], files[i]["title"], files[i]["link"], )
        output_file = open("../Relex12.github.io/{}".format(files[i]["output"]), 'w')
        print(files[i]["output"])
        output_file.write(front_matter + input_file.read())
    else:
        print("Cannot create {}, {}/{} is missing.".format(files[i]["output"], files[i]["folder"], files[i]["file"]) )
