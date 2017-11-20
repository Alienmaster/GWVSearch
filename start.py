"""
Startdatei
"""
import main
import astar
reihenfolge = ['u', 'r', 'd', 'l']
def start(filename, search):
    """
    Startmethode
    """
    tp1 = []
    tp2 = []
    var_sp = []
    maze = main.readmaze(filename)
    var_sp = main.analyse(maze, "s")
    var_gp = main.analyse(maze, "g")
    tp1 = main.analyse(maze, "1")
    tp2 = main.analyse(maze, "2")
    try:
        if search == "depth":
            main.dfs(var_sp, var_gp, tp1, tp2)
        elif search == "breadth":
            main.bfs(var_sp, var_gp, tp1, tp2)
        elif search == "astar":
            astar.astar(var_sp, var_gp, tp1, tp2)
    except IndexError:
        print("Es gibt keinen gültigen Pfad.")

start("testmaze.txt", "astar")
