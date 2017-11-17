import copy
import time
from heapq import heappush, heappop
import main
import output

def astar(sp, gp, tp1, tp2, order):
    """
    A* Suche. Jeder Knoten in der Nachbarschaft wird untersucht und
    zum Heap hinzugefügt mit der dazugehörigen Euklidischen Distanz.
    Danach wird der kleinste Wert als neue x und y erstellt.
    """
    print(main.euklidischedistanz(sp, gp))
    ###
    x = sp[0]
    y = sp[1]
    nextmove = []
    # stack = [[[x, y]]]
    # var_c = []
    heap = []
    #heappush(heap, (euklid, x, y))
    while True:
        if main.goalnotreached(x, y):
            main.setmarker(x, y)
            actualorder = copy.deepcopy(order)
            while len(actualorder) != 0:
                nextstep = 0
                nextstep = actualorder.pop(0)
                if main.neighbourfree(nextstep , x, y):
                    arrow = main.direction(nextstep, x, y)
                    euklid = main.euklidischedistanz(arrow, gp)
                    print(euklid)
                    heappush(heap, (euklid, arrow[0], arrow[1]))
            # print(heappop(heap))
            nextmove = (heappop(heap))
            x = nextmove[1]
            y = nextmove[2]
            print(nextmove[2])
            output.printstate()
            time.sleep(.10)
        else:
            break

        # else:
        #     print(stack[0])
        #     output.printfinalstate(sp, gp, stack)
        #     break
