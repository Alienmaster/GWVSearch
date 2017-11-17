"""
GWV Uebung 2017
Sebastian Stelter
Florian Schmalzl
Robert Geislinger
"""
import copy
import time
import output
#Labyrinth
MAZE = [[]]
#Labyrinth einlesen
def readmaze(filename):
    """
    Textfile wird eingelesen und als Array returnd
    """
    with open(filename) as var_f:
        var_m = 0
        for line in var_f:
            var_n = 0
            while var_n < len(line):
                if line[var_n] != "\n":
                    MAZE[var_m].append(line[var_n])
                var_n += 1
            MAZE.append([])
            var_m += 1
        MAZE.pop()
    return MAZE

def setmarker(var_x, var_y):
    """
    Setzt eine Markierung "o" auf der aktuellen Position
    """
    MAZE[var_x][var_y] = 'o'

def goalnotreached(var_x, var_y):
    """
    Ueberpruefung ob wir schon beim Ziel sind
    """
    return MAZE[var_x][var_y] != 'g'

def neighbourfree(var_d, var_x, var_y):
    """Ueberprueft in die jeweilige Richtung ob frei ist.
    Uebergeben wird die Richtung (up, down, left right)
    und der Switchcase gibt True/False zurueck"""
    d = direction(var_d, var_x, var_y)
    return 'o' != MAZE[d[0]][d[1]] != 'x'

def portal(x, y, tp):
    """
    Bekommt die aktuellen Koordinaten und gibt das
    andere Portal zurueck
    """
    var_portalend = []
    print("X", x, y)
    if tp[0] == x and tp[1] == y:
        var_portalend.append(tp[2])
        var_portalend.append(tp[3])
    else:
        var_portalend.append(tp[0])
        var_portalend.append(tp[1])
    return var_portalend

def dfs(var_sp, var_gp, tp1, tp2):
    """
    Tiefensuche
    """
    var_x = var_sp[0]
    var_y = var_sp[1]
    stack = []
    stack.append(var_x)
    stack.append(var_y)
    #reihenfolge = ['u', 'r', 'd', 'l']
    while True:
        if goalnotreached(var_x, var_y):
            if neighbourfree('u', var_x, var_y):
                stack.append(var_x-1)
                stack.append(var_y)
            elif neighbourfree('r', var_x, var_y):
                stack.append(var_x)
                stack.append(var_y+1)
            elif neighbourfree('d', var_x, var_y):
                stack.append(var_x+1)
                stack.append(var_y)
            elif neighbourfree('l', var_x, var_y):
                stack.append(var_x)
                stack.append(var_y-1)
            else:
                stack.pop()
                stack.pop()
            if MAZE[stack[-2]][stack[-1]] == '1':
                portalend = portal(stack[-2], stack[-1], tp1)
                stack.append(portalend[0])
                stack.append(portalend[1])
            elif MAZE[stack[-2]][stack[-1]] == '2':
                portalend(stack[-2], stack[-1], tp2)
                stack.append(portalend[0])
                stack.append(portalend[1])
            setmarker(var_x, var_y)
            var_y = stack[-1]
            var_x = stack[-2]
            output.printstate()
            print(stack)
            print(var_x)
            print(var_y)
            time.sleep(.10)
        else:
            if len(stack) == 0:
                print("Kein Weg zum Ziel gefunden")
                break
            output.printfinalstate(var_sp, var_gp, stack)
            break

def bfs(var_sp, var_gp, var_tp1, var_tp2):
    """
    Breitensuche
    """
    x = var_sp[0]
    y = var_sp[1]
    stack = [[[x, y]]]
    var_c = []
    i = 0
    while True:
        if goalnotreached(x, y):
            setmarker(x, y)
            if neighbourfree('u', x, y):
                var_c = copy.deepcopy(stack[0])
                var_c.append([x-1, y])
                stack.append(var_c)
            if neighbourfree('r', x, y):
                var_c = copy.deepcopy(stack[0])
                var_c.append([x, y+1])
                stack.append(var_c)
            if neighbourfree('d', x, y):
                var_c = copy.deepcopy(stack[0])
                var_c.append([x+1, y])
                stack.append(var_c)
            if neighbourfree('l', x, y):
                var_c = copy.deepcopy(stack[0])
                var_c.append([x, y-1])
                stack.append(var_c)
            """
            if MAZE[1][9] == '1':
                print(stack, stack[0][-1][1])
                break
                portalend = portal(stack[0][-1][0], stack[0][-1][1], var_tp1)
                var_c = copy.deepcopy(stack[0])
                var_c.append([portalend[0], portalend[1]])
                stack.append(var_c)
            elif MAZE[stack[-2]][stack[-1]] == '2':
                portal(stack[-2], stack[-1], var_tp2)
                stack.append(gp[0])
                stack.append(gp[1])
            """
            stack.pop(0)
            x = stack[0][-1][0]
            y = stack[0][-1][1]
            output.printstate()
            print(x)
            print(y)
            i += 1
        else:
            print(stack[0])
            output.printfinalstate(var_sp, var_gp, stack)
            break

def analyse(maze, char):
    """
    Durchsucht das Array nach dem char und gibt eine Liste zurueck
    """
    i = 0
    j = 0
    charlist = []
    mazerows = len(MAZE)
    mazecols = len(MAZE[0])
    while i < mazerows-1:
        while j < mazecols-1:
            if MAZE[i][j] == char:
                charlist.append(i)
                charlist.append(j)
            j += 1
        j = 0
        i += 1
    return charlist

def direction(arrow, x, y):
    """
    Wandelt die Richtung in ein neuen x und y Wert
    """
    directionarray = []
    if arrow == 'u':
        x -= 1
    elif arrow == 'r':
        y += 1
    elif arrow == 'd':
        x += 1
    elif arrow == 'l':
        y -= 1
    directionarray.append(x)
    directionarray.append(y)
    return directionarray

def euklidischedistanz(sp, gp):
    """
    Berechnet die Euklidische Distanz zwischen zwei Feldern.
    Übergeben werden eine Liste mit Startund Zielkoordinaten ([0] = x, [1] = y)
    Rückgabewert ist die Euklidische Distanz als int
    """
    return abs((sp[0]-gp[0])+(sp[1]-gp[1]))
