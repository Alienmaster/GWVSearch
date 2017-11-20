"""
Alle Funktionen zur GUI-Ausgabe des Labyrinths
"""
import inspect
import main
def printstate():
    """
    Ausgabe des aktuellen Status
    """
    for x in range(0, len(main.MAZE)):
        s = ""
        for y in range(0, len(main.MAZE[x])):
            s = s + main.MAZE[x][y]
        print(s)

def printfinalstate(var_sp, var_gp, stack):
    """
    Druckt den finalen Weg aus
    """
    if inspect.stack()[1][3] == "bfs":
        for i in range(0, len(stack[0])):
            main.MAZE[stack[0][i][0]][stack[0][i][1]] = '*'
            i += 1
    elif inspect.stack()[1][3] == "astar":
        for i in range(0, len(stack[0][4])):
            main.MAZE[stack[0][4][i][0]][stack[0][4][i][1]] = '*'
            i += 1
    main.MAZE[var_sp[0]][var_sp[1]] = 'S'
    main.MAZE[var_gp[0]][var_gp[1]] = 'G'
    printstate()
    #print(x)
    #print(y)
