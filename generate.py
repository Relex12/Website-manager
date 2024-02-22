from os import path
from os import system

if (not path.exists("../Relex12.github.io/")):
    raise FileNotFoundError("Relex12.github.io directory not found")
if (not path.exists("../Markdown-Table-of-Contents/")):
    raise FileNotFoundError("Markdown-Table-of-Contents directory not found")

#####################
# FILES DECLARATION #
#####################

files = [
{"folder": "3PBDH", "file":"README.md", "layout": "default",
"title": "3PBDH - Pairing based Diffie-Hellman", "link": "fr/3PBDH", "output": "3PBDH.md"},
{"folder": "Decentralized-Password-Manager", "file":"README.md", "layout": "default",
"title": "Decentralized-Password-Manager", "link": "fr/Decentralized-Password-Manager", "output": "Decentralized-Password-Manager.md"},
{"folder": "Decentralized-Password-Manager", "file":"readme/01-FR-comparatif.md", "layout": "default",
"title": "Comparatif", "link": "fr/Decentralized-Password-Manager/Comparatif", "output": "Decentralized-Password-Manager.01-FR-comparatif.md"},
{"folder": "Decentralized-Password-Manager", "file":"readme/02-FR-solutions.md", "layout": "default",
"title": "Comparatif", "link": "fr/Decentralized-Password-Manager/Solutions", "output": "Decentralized-Password-Manager.02-FR-solutions.md"},
{"folder": "Decentralized-Password-Manager", "file":"readme/03-FR-specifications.md", "layout": "default",
"title": "Comparatif", "link": "fr/Decentralized-Password-Manager/Specifications", "output": "Decentralized-Password-Manager.03-FR-specifications.md"},
{"folder": "Decentralized-Password-Manager", "file":"readme/04-FR-implementation.md", "layout": "default",
"title": "Comparatif", "link": "fr/Decentralized-Password-Manager/Implementation", "output": "Decentralized-Password-Manager.04-FR-implementation.md"},
{"folder": "Decentralized-Password-Manager", "file":"readme/05-FR-fonctionnalites.md", "layout": "default",
"title": "Comparatif", "link": "fr/Decentralized-Password-Manager/Comparatif", "output": "Decentralized-Password-Manager.05-FR-fonctionnalites.md"},
{"folder": "Dictionaries", "file":"README.md", "layout": "default",
"title": "Dictionaries", "link": "Dictionaries", "output": "Dictionaries.md"},
{"folder": "Dictionaries", "file":"README-fr.md", "layout": "default",
"title": "Dictionaries", "link": "fr/Dictionaries", "output": "Dictionaries-fr.md"},
{"folder": "Genex", "file":"README.md", "layout": "default",
"title": "Genex", "link": "fr/Genex", "output": "Genex.md"},
{"folder": "Introduction-to-Computer-Science", "file":"README.md", "layout": "default",
"title": "Introduction to Computer Science", "link": "fr/Introduction-to-Computer-Science", "output": "Introduction-to-Computer-Science.md"},
{"folder": "Languages", "file":"README.md", "layout": "default",
"title": "Languages", "link": "fr/Languages", "output": "Languages.md"},
{"folder": "Languages", "file":"Sheets/Bash-Unix.md", "layout": "default",
"title": "Bash Unix", "link": "fr/Languages/Bash-Unix", "output": "Languages.Bash-Unix.md"},
{"folder": "Languages", "file":"Sheets/DOT.md", "layout": "default",
"title": "DOT", "link": "fr/Languages/DOT", "output": "Languages.DOT.md"},
{"folder": "Languages", "file":"Sheets/Docker.md", "layout": "default",
"title": "Docker", "link": "fr/Languages/Docker", "output": "Languages.Docker.md"},
{"folder": "Languages", "file":"Sheets/Git.md", "layout": "default",
"title": "Git", "link": "fr/Languages/Git", "output": "Languages.Git.md"},
{"folder": "Languages", "file":"Sheets/GDB.md", "layout": "default",
"title": "GDB", "link": "fr/Languages/GDB", "output": "Languages.GDB.md"},
{"folder": "Languages", "file":"Examples/Markdown.md", "layout": "default",
"title": "Markdown", "link": "fr/Languages/Markdown", "output": "Languages.Markdown.md"},
{"folder": "Languages", "file":"Sheets/JavaScript.md", "layout": "default",
"title": "JavaScript", "link": "fr/Languages/JavaScript", "output": "Languages.JavaScript.md"},
{"folder": "Lining-draw", "file":"README.md", "layout": "default",
"title": "Lining draw", "link": "Lining-draw", "output": "Lining-draw.md"},
{"folder": "Lining-draw", "file":"README-fr.md", "layout": "default",
"title": "Lining draw", "link": "fr/Lining-draw", "output": "Lining-draw-fr.md"},
{"folder": "Loup-garou", "file":"README.md", "layout": "default",
"title": "Loup-garou", "link": "fr/Loup-garou", "output": "Loup-garou.md"},
{"folder": "Markdown-Table-of-Contents", "file":"README.md", "layout": "default",
"title": "Markdown Table of Contents", "link": "Markdown-Table-of-Contents", "output": "Markdown-Table-of-Contents.md"},
{"folder": "Markdown-Table-of-Contents", "file":"README-fr.md", "layout": "default",
"title": "Markdown Table of Contents", "link": "fr/Markdown-Table-of-Contents", "output": "Markdown-Table-of-Contents-fr.md"},
{"folder": "Maths-for-IT", "file":"README.md", "layout": "default",
"title": "Maths for IT", "link": "fr/Maths-for-IT", "output": "Maths-for-IT.md"},
{"folder": "Maths-for-IT", "file":"readme/01-FR-Problemes-Mathematiques.md", "layout": "default",
"title": "Problèmes mathématiques", "link": "fr/Maths-for-IT/Problemes-Mathematiques", "output": "Maths-for-IT.01-FR-Problemes-Mathematiques.md"},
{"folder": "Maths-for-IT", "file":"readme/02-FR-Intelligence-Artificielle.md", "layout": "default",
"title": "Intelligence artificielle", "link": "fr/Maths-for-IT/Intelligence-Artificielle", "output": "Maths-for-IT.02-FR-Intelligence-Artificielle.md"},
{"folder": "Maths-for-IT", "file":"readme/03-FR-Algorithmes.md", "layout": "default",
"title": "Algorithmes", "link": "fr/Maths-for-IT/Algorithmes", "output": "Maths-for-IT.03-FR-Algorithmes.md"},
{"folder": "Maths-for-IT", "file":"readme/04-FR-Cryptographie.md", "layout": "default",
"title": "Cryptographie", "link": "fr/Maths-for-IT/Cryptographie", "output": "Maths-for-IT.04-FR-Cryptographie.md"},
{"folder": "Maths-for-IT", "file":"readme/05-FR-Structures-De-Donnees.md", "layout": "default",
"title": "Structures de données", "link": "fr/Maths-for-IT/Structures-De-Donnees", "output": "Maths-for-IT.05-FR-Structures-De-Donnees.md"},
{"folder": "Maths-for-IT", "file":"readme/06-FR-Generation-De-Nombres-Aleatoires.md", "layout": "default",
"title": "Génération de nombres aléatoires", "link": "fr/Maths-for-IT/Generation-De-Nombres-Aleatoires", "output": "Maths-for-IT.06-FR-Generation-De-Nombres-Aleatoires.md"},
{"folder": "Maths-for-IT", "file":"readme/07-FR-Compilation.md", "layout": "default",
"title": "Compilation", "link": "fr/Maths-for-IT/Compilation", "output": "Maths-for-IT.07-FR-Compilation.md"},
{"folder": "Maths-for-IT", "file":"readme/08-FR-Constantes-Fondamentales.md", "layout": "default",
"title": "Constantes fondamentales", "link": "fr/Maths-for-IT/Constantes-Fondamentales", "output": "Maths-for-IT.08-FR-Constantes-Fondamentales.md"},
{"folder": "Relex12", "file":"README.md", "layout": "default",
"title": "Relex12 - Adrian Bonnet", "link": "null", "output": "index.md"},
{"folder": "Secret-Santa", "file":"README.md", "layout": "default",
"title": "Secret Santa", "link": "fr/Secret-Santa", "output": "Secret-Santa.md"},
{"folder": "Simple-Progress-Bar", "file":"README.md", "layout": "default",
"title": "Simple Progress Bar", "link": "Simple-Progress-Bar", "output": "Simple-Progress-Bar.md"},
{"folder": "Simple-Progress-Bar", "file":"README-fr.md", "layout": "default",
"title": "Simple Progress Bar", "link": "fr/Simple-Progress-Bar", "output": "Simple-Progress-Bar-fr.md"},
{"folder": "Voting-Systems-Comparison", "file":"README.md", "layout": "default",
"title": "Voting Systems Comparison", "link": "fr/Voting-Systems-Comparison", "output": "Voting-Systems-Comparison.md"},
{"folder": "Voting-Systems-Simulation", "file":"README.md", "layout": "default",
"title": "Voting Systems Simulation", "link": "Voting-Systems-Simulation", "output": "Voting-Systems-Simulation.md"},
{"folder": "Voting-Systems-Simulation", "file":"README-fr.md", "layout": "default",
"title": "Voting Systems Simulation", "link": "fr/Voting-Systems-Simulation", "output": "Voting-Systems-Simulation-fr.md"},
{"folder": "Voting-Systems-Simulation", "file":"doc/simulation.html", "layout": "null",
"title": "Voting Systems Simulation Doc", "link": "Voting-Systems-Simulation/doc/simulation", "output": "Voting-Systems-Simulation.doc.simulation.html"},
{"folder": "Voting-Systems-Simulation", "file":"doc/voting.html", "layout": "null",
"title": "Voting Systems Simulation Doc", "link": "Voting-Systems-Simulation/doc/voting", "output": "Voting-Systems-Simulation.doc.voting.html"},
{"folder": "Website-manager", "file":"README.md", "layout": "default",
"title": "Website manager", "link": "Website-manager", "output": "Website-manager.md"},
{"folder": "Word-machine", "file":"README.md", "layout": "default",
"title": "Word Machine", "link": "Word-machine", "output": "Word-machine.md"},
{"folder": "Wikipedia-Translate-Crawler", "file":"README.md", "layout": "default",
"title": "Wikipedia Translate Crawler", "link": "Wikipedia-Translate-Crawler", "output": "Wikipedia-Translate-Crawler.md"},
{"folder": "Wikipedia-Translate-Crawler", "file":"README-fr.md", "layout": "default",
"title": "Wikipedia Translate Crawler", "link": "fr/Wikipedia-Translate-Crawler", "output": "Wikipedia-Translate-Crawler-fr.md"},
{"folder": "Word-machine", "file":"doc/dictionary.html", "layout": "null",
"title": "Word Machine Doc", "link": "Word-machine/doc/dictionary", "output": "Word-machine.doc.dictionary.html"},
{"folder": "Word-machine", "file":"doc/generation.html", "layout": "null",
"title": "Word Machine Doc", "link": "Word-machine/doc/generation", "output": "Word-machine.doc.generation.html"},
{"folder": "Word-machine", "file":"doc/word-machine.html", "layout": "null",
"title": "Word Machine Doc", "link": "Word-machine/doc/word-machine", "output": "Word-machine.doc.word-machine.html"},
]


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
