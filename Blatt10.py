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
#Dictionary SatzAnfang
dSatzAnfang = defaultdict(int)

#Wortliste einlesen
def importfile(filename):
    """
    Trainingsdatenfile wird eingelesen
    """
    beginning = ""
    count = 0
    with open(filename, encoding="utf8") as var_f:
        for line in var_f:
            line = re.sub('\n$', '', line)
            #print(beginning)
            if not beginning:
                line = re.sub('.*\t', '', line)
                dSatzAnfang[line] +=1
                count +=1
                #print(line)
            beginning = line
    print(dSatzAnfang["NN"])        
            
importfile("hdt-1-10000-train.tags")

#with open('data.json', 'w') as fp:
#    json.dump(d, fp)

def weighted_random_by_dct(dct):
    rand_val = random.random()
    total = 0
    for k, v in dct.items():
        total += v
        if rand_val <= total:
            return k
    assert False, 'unreachable'
    
weighted_random_by_dct(dSatzAnfang)