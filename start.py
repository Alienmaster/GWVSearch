"""
Startdatei
"""
import main
import astar

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
    if search == "depth":
        main.dfs(var_sp, var_gp, tp1, tp2)
    elif search == "breath":
        main.bfs(var_sp, var_gp, tp1, tp2)
    elif search == "astar":
        astar.astar(var_sp, var_gp, tp1, tp2)

start("testmaze.txt", "astar")
