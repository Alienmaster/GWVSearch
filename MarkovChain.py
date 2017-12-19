"""
GWV Uebung 2017
Sebastian Stelter
Florian Schmalzl
Robert Geislinger
"""
from collections import defaultdict
import re
import json
import random
#Dictionary
d = defaultdict(list)
#Wortliste einlesen
def importfile(filename):
    """
    Textfile wird eingelesen und als Dictionary abgelegt
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

#Ausgabe Beispielliste für das Wort "ich"
#print(d["ich"])
#Zähler wieviele Worte ausgegeben werden sollen
acc = 15
#Anfangswort
start = "Mama"
print(start, end=" ")
try:
    while acc != 0:
        word = random.choice(d[start])
        print(word, end=" ")
        acc = acc-1
        start = word
except: print ("Wort nicht enthalten")