from os import path
from os import system

if (not path.exists("../Relex12.github.io/")):
    raise FileNotFoundError("Relex12.github.io directory not found")
if (not path.exists("../Markdown-Table-of-Contents/")):
    raise FileNotFoundError("Markdown-Table-of-Contents directory not found")


# Dictionaries

if (path.exists("../Dictionaries/")):
    system("python3 ../Markdown-Table-of-Contents/toc.py ../Dictionaries/README.md")
    input_file = open("../Dictionaries/README.md", 'r')
    front_matter = """---
layout: default
title: "Dictionaries"
permalink: Dictionaries
---

"""
    output_file = open("../Relex12.github.io/Dictionaries.md", 'w')
    output_file.write(front_matter + input_file.read())

    system("python3 ../Markdown-Table-of-Contents/toc.py ../Dictionaries/README-fr.md")
    input_file = open("../Dictionaries/README-fr.md", 'r')
    front_matter = """---
layout: default
title: "Dictionaries"
permalink: fr/Dictionaries
---

"""
    output_file = open("../Relex12.github.io/Dictionaries-fr.md", 'w')
    output_file.write(front_matter + input_file.read())

# Genex

if (path.exists("../Genex/")):
    system("python3 ../Markdown-Table-of-Contents/toc.py ../Genex/README.md")
    input_file = open("../Genex/README.md", 'r')
    front_matter = """---
layout: default
title: "Genex"
permalink: fr/Genex
---

"""
    output_file = open("../Relex12.github.io/Genex.md", 'w')
    output_file.write(front_matter + input_file.read())

# Introduction-to-Computer-Science

if (path.exists("../Introduction-to-Computer-Science/")):
    system("python3 ../Markdown-Table-of-Contents/toc.py ../Introduction-to-Computer-Science/README.md")
    input_file = open("../Introduction-to-Computer-Science/README.md", 'r')
    front_matter = """---
layout: default
title: "Introduction to Computer Science"
permalink: fr/Introduction-to-Computer-Science
---

"""
    output_file = open("../Relex12.github.io/Introduction-to-Computer-Science.md", 'w')
    output_file.write(front_matter + input_file.read())


# Languages

if (path.exists("../Languages/")):
    system("python3 ../Markdown-Table-of-Contents/toc.py ../Languages/README.md")
    input_file = open("../Languages/README.md", 'r')
    front_matter = """---
layout: default
title: "Languages"
permalink: fr/Languages
---

"""
    output_file = open("../Relex12.github.io/Languages.md", 'w')
    output_file.write(front_matter + input_file.read())

## Bash-Unix

    system("python3 ../Markdown-Table-of-Contents/toc.py ../Languages/Sheets/Bash-Unix.md")
    input_file = open("../Languages/Sheets/Bash-Unix.md", 'r')
    front_matter = """---
layout: default
title: "Bash Unix"
permalink: fr/Languages/Bash-Unix
---

"""
    output_file = open("../Relex12.github.io/Languages.Bash-Unix.md", 'w')
    output_file.write(front_matter + input_file.read())

## DOT

    system("python3 ../Markdown-Table-of-Contents/toc.py ../Languages/Sheets/DOT.md")
    input_file = open("../Languages/Sheets/DOT.md", 'r')
    front_matter = """---
layout: default
title: "DOT"
permalink: fr/Languages/DOT
---

"""
    output_file = open("../Relex12.github.io/Languages.DOT.md", 'w')
    output_file.write(front_matter + input_file.read())

## Git

    system("python3 ../Markdown-Table-of-Contents/toc.py ../Languages/Sheets/Git.md")
    input_file = open("../Languages/Sheets/Git.md", 'r')
    front_matter = """---
layout: default
title: "Git"
permalink: fr/Languages/Git
---

"""
    output_file = open("../Relex12.github.io/Languages.Git.md", 'w')
    output_file.write(front_matter + input_file.read())

## GDB

    system("python3 ../Markdown-Table-of-Contents/toc.py ../Languages/Sheets/GDB.md")
    input_file = open("../Languages/Sheets/GDB.md", 'r')
    front_matter = """---
layout: default
title: "GDB"
permalink: fr/Languages/GDB
---

"""
    output_file = open("../Relex12.github.io/Languages.GDB.md", 'w')
    output_file.write(front_matter + input_file.read())

## Markdown

    input_file = open("../Languages/Examples/Markdown.md", 'r')
    front_matter = """---
layout: default
title: "Markdown"
permalink: fr/Languages/Markdown
---

"""
    output_file = open("../Relex12.github.io/Languages.Markdown.md", 'w')
    output_file.write(front_matter + input_file.read())

## JavaScript

    system("python3 ../Markdown-Table-of-Contents/toc.py ../Languages/Sheets/JavaScript.md")
    input_file = open("../Languages/Sheets/JavaScript.md", 'r')
    front_matter = """---
layout: default
title: "JavaScript"
permalink: fr/Languages/JavaScript
---

"""
    output_file = open("../Relex12.github.io/Languages.JavaScript.md", 'w')
    output_file.write(front_matter + input_file.read())

# Lining-draw

if (path.exists("../Lining-draw/")):
    system("python3 ../Markdown-Table-of-Contents/toc.py ../Lining-draw/README.md")
    input_file = open("../Lining-draw/README.md", 'r')
    front_matter = """---
layout: default
title: "Lining draw"
permalink: Lining-draw
---

"""
    output_file = open("../Relex12.github.io/Lining-draw.md", 'w')
    output_file.write(front_matter + input_file.read())

    system("python3 ../Markdown-Table-of-Contents/toc.py ../Lining-draw/README-fr.md")
    input_file = open("../Lining-draw/README-fr.md", 'r')
    front_matter = """---
layout: default
title: "Lining draw"
permalink: fr/Lining-draw
---

"""
    output_file = open("../Relex12.github.io/Lining-draw-fr.md", 'w')
    output_file.write(front_matter + input_file.read())

# Loup-garou

if (path.exists("../Loup-garou/")):
    system("python3 ../Markdown-Table-of-Contents/toc.py ../Loup-garou/README.md")
    input_file = open("../Loup-garou/README.md", 'r')
    front_matter = """---
layout: default
title: "Loup-garou"
permalink: fr/Loup-garou
---

"""
    output_file = open("../Relex12.github.io/Loup-garou.md", 'w')
    output_file.write(front_matter + input_file.read())

# Markdown-Table-of-Contents

if (path.exists("../Markdown-Table-of-Contents/")):
    system("python3 ../Markdown-Table-of-Contents/toc.py ../Markdown-Table-of-Contents/README.md")
    input_file = open("../Markdown-Table-of-Contents/README.md", 'r')
    front_matter = """---
layout: default
title: "Markdown Table of Contents"
permalink: Markdown-Table-of-Contents
---

"""
    output_file = open("../Relex12.github.io/Markdown-Table-of-Contents.md", 'w')
    output_file.write(front_matter + input_file.read())

    system("python3 ../Markdown-Table-of-Contents/toc.py ../Markdown-Table-of-Contents/README-fr.md")
    input_file = open("../Markdown-Table-of-Contents/README-fr.md", 'r')
    front_matter = """---
layout: default
title: "Markdown Table of Contents"
permalink: fr/Markdown-Table-of-Contents
---

"""
    output_file = open("../Relex12.github.io/Markdown-Table-of-Contents-fr.md", 'w')
    output_file.write(front_matter + input_file.read())

# Maths_for_IT

if (path.exists("../Maths_for_IT/")):
    system("python3 ../Markdown-Table-of-Contents/toc.py ../Maths_for_IT/README.md")
    input_file = open("../Maths_for_IT/README.md", 'r')
    front_matter = """---
layout: default
title: "Maths for IT"
permalink: fr/Maths-for-IT
---

"""
    output_file = open("../Relex12.github.io/Maths_for_IT.md", 'w')
    output_file.write(front_matter + input_file.read())

# Relex12

if (path.exists("../Relex12/")):
    system("python3 ../Markdown-Table-of-Contents/toc.py ../Relex12/README.md")
    input_file = open("../Relex12/README.md", 'r')
    front_matter = """---
layout: default
title: "Relex12 - Adrian Bonnet"
---

"""
    output_file = open("../Relex12.github.io/index.md", 'w')
    output_file.write(front_matter + input_file.read())

# Secret-Santa

if (path.exists("../Secret-Santa/")):
    system("python3 ../Markdown-Table-of-Contents/toc.py ../Secret-Santa/README.md")
    input_file = open("../Secret-Santa/README.md", 'r')
    front_matter = """---
layout: default
title: "Secret Santa"
permalink: fr/Secret-Santa
---

"""
    output_file = open("../Relex12.github.io/Secret-Santa.md", 'w')
    output_file.write(front_matter + input_file.read())

# Simple-Progress-Bar

if (path.exists("../Simple-Progress-Bar/")):
    system("python3 ../Markdown-Table-of-Contents/toc.py ../Simple-Progress-Bar/README.md")
    input_file = open("../Simple-Progress-Bar/README.md", 'r')
    front_matter = """---
layout: default
title: "Simple-Progress-Bar"
permalink: Simple-Progress-Bar
---

"""
    output_file = open("../Relex12.github.io/Simple-Progress-Bar.md", 'w')
    output_file.write(front_matter + input_file.read())

    system("python3 ../Markdown-Table-of-Contents/toc.py ../Simple-Progress-Bar/README-fr.md")
    input_file = open("../Simple-Progress-Bar/README-fr.md", 'r')
    front_matter = """---
layout: default
title: "Simple-Progress-Bar"
permalink: fr/Simple-Progress-Bar
---

"""
    output_file = open("../Relex12.github.io/Simple-Progress-Bar-fr.md", 'w')
    output_file.write(front_matter + input_file.read())

# Voting-Systems-Comparison

if (path.exists("../Voting-Systems-Comparison/")):
    system("python3 ../Markdown-Table-of-Contents/toc.py ../Voting-Systems-Comparison/README.md")
    input_file = open("../Voting-Systems-Comparison/README.md", 'r')
    front_matter = """---
layout: default
title: "Voting Systems Comparison"
permalink: fr/Voting-Systems-Comparison
---

"""
    output_file = open("../Relex12.github.io/Voting-Systems-Comparison.md", 'w')
    output_file.write(front_matter + input_file.read())

# Word_machine

if (path.exists("../Word_machine/")):
    system("python3 ../Markdown-Table-of-Contents/toc.py ../Word_machine/README.md")
    input_file = open("../Word_machine/README.md", 'r')
    front_matter = """---
layout: default
title: "Word Machine"
permalink: Word-machine
---

"""
    output_file = open("../Relex12.github.io/Word_machine.md", 'w')
    output_file.write(front_matter + input_file.read())

## Init

    system("python3 ../Markdown-Table-of-Contents/toc.py ../Word_machine/doc/__init__.html")
    input_file = open("../Word_machine/doc/__init__.html", 'r')
    front_matter = """---
title: "Word Machine Doc"
permalink: Word-machine/doc/init
---

"""
    output_file = open("../Relex12.github.io/Word_machine.doc.init.html", 'w')
    output_file.write(front_matter + input_file.read())

## Dictionary processing
    system("python3 ../Markdown-Table-of-Contents/toc.py ../Word_machine/doc/dictionary_processing.html")
    input_file = open("../Word_machine/doc/dictionary_processing.html", 'r')
    front_matter = """---
title: "Word Machine Doc"
permalink: Word-machine/doc/dictionary-processing
---

"""
    output_file = open("../Relex12.github.io/Word_machine.doc.dictionary_processing.html", 'w')
    output_file.write(front_matter + input_file.read())

## Word machine
    system("python3 ../Markdown-Table-of-Contents/toc.py ../Word_machine/doc/word_machine.html")
    input_file = open("../Word_machine/doc/word_machine.html", 'r')
    front_matter = """---
title: "Word Machine Doc"
permalink: Word-machine/doc/word-machine
---

"""
    output_file = open("../Relex12.github.io/Word_machine.doc.word_machine.html", 'w')
    output_file.write(front_matter + input_file.read())
