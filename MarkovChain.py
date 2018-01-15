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
dSatzanfang = {}
dFollowing = {}

#Wortliste einlesen
def importfile(filename):
    """
    Trainingsdatenfile wird eingelesen
    """
    beginning = ""
    count = 0
    v1 = ''
    first = True
    with open(filename, encoding="utf8") as var_f:
        for line in var_f:
            line = re.sub('\n$', '', line)
            if line == '':
            	count = 0
            	continue
            l2 = line.split()
            if first:
            	v1 = l2[len(l2)-1]
            	first = False
            #print(l2)
            k = l2[0]
            v2 = l2[len(l2)-1]
            if count == 0:
            	dSatzanfang.update({k:v2})
            	count += 1
            if v1 in dFollowing:
            	dFollowing[v1].append(v2)
            else:
            	dFollowing.update({v1:[v2]})
            v1 = v2
        #print(dFollowing["$."])
    #for key, value in dFollowing.items():
    #	print(key)
    #print("------")
    #for key, value in dSatzanfang.items():
    #	print(key)


     
            


#with open('data.json', 'w') as fp:
#    json.dump(d, fp)
def getRandomTag(tag):
	r = random.randint(0, len(dFollowing[tag])-1)
	l = dFollowing[tag]
	return l[r]

def getRandomTagAnfang():
	r = random.choice(list(dSatzanfang.keys()))
	l = dSatzanfang[r]
	return l
    




def processInput():
	raw = input("Please give me some text to work with.")
	words  = raw.split()
	newwords = []
	for w in range(0, len(words)):
		if words[w].isalpha():
			newwords.append(words[w])
		else:
			chars = list(words[w])
			worda = []
			for c in chars:
				#print(c)
				if c.isalpha():
					worda.append(c)
				else:
					if not worda == []:
						newwords.append("".join(str(x) for x in worda))
						worda.clear()
					newwords.append(str(c))
			if not worda == []:
				newwords.append("".join(str(x) for x in worda))

		#print(newwords)
	tagwords(newwords)

def tagwords(words):
	first = True
	out = []
	for w in words:
		out.append(w)
		#print(out)
		if first:
			if w in dSatzanfang:
				tag = dSatzanfang[w]
			else: 
				tag = getRandomTagAnfang()
			first = False
			out.append(tag)
		else:
			if tag in dFollowing:
				tag2 = getRandomTag(tag)
			else:
				tag2 = "NN"
			out.append(tag2)
			tag = tag2
	print(out)



importfile("hdt-1-10000-train.tags")
#print(dSatzanfang)
processInput()