"""
GWV Uebung 2017
Sebastian Stelter
Florian Schmalzl
Robert Geislinger
"""
from collections import defaultdict
import re
import json
#Labyrinth
d = defaultdict(list)
#Labyrinth einlesen
def importfile(filename):
    """
    Textfile wird eingelesen und als Array returnd
    """
    with open(filename, encoding="utf8") as var_f:
        firstline = ""
        for line in var_f:
            line = re.sub('\n$', '', line)
            value = d[firstline]
            value.append(line)
            d[firstline] = value
            firstline = line
            #print(value)

importfile("ggcc-one-word-per-line.txt")

#with open('data.json', 'w') as fp:
#    json.dump(d, fp)

print(len(d))
print(d["ich"])