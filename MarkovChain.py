"""
GWV Uebung 2017
Sebastian Stelter
Florian Schmalzl
Robert Geislinger
"""
#Labyrinth
d = {}
#Dateiliste einlesen
def readfile(filename, encoding='UTF8'):
    """
    Textfile wird eingelesen und als Array returnd
    """
    with open(filename) as var_f:
        firstline = ""
        
        for line in var_f:
            try:
                #d[firstline] = line
                #firstline = line
                #print(len(d))
                print(line)
            except:
                continue
        len(d)
readfile("ggcc-one-word-per-line.txt")
len(d)
