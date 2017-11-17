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
    ###
    x = sp[0]
    y = sp[1]
    nextmove = []
    # stack = [[[x, y]]]
    # var_c = []
    heap = []
    heappush(heap, (gp[0]-x+gp[1]-y,0, x, y))
    #heappush(heap, (euklid, x, y))
    while True:
        if main.goalnotreached(x, y):
            main.setmarker(x, y)
            if(main.neighbourfree('u', x, y)):
                euklid = gp[0] - (x-1) + (gp[1] - y)
                heappush(heap, (heap[0][1]+euklid,heap[0][1]+1, x-1, y))
            if(main.neighbourfree('r', x, y)):
                euklid = gp[0] - x + (gp[1] - (y+1))
                heappush(heap, (heap[0][1]+euklid,heap[0][1]+1, x, y+1))
            if(main.neighbourfree('d', x, y)):
                euklid = gp[0] - (x+1) + (gp[1] - y)
                heappush(heap, (heap[0][1]+euklid,heap[0][1]+1, x+1, y))
            if(main.neighbourfree('l', x, y)):
                euklid = gp[0] - x + (gp[1] - (y-1))
                heappush(heap, (heap[0][1]+euklid,heap[0][1]+1, x, y-1))
            x = heap[0][2]
            y = heap[0][3]
            heappop(heap)
            print(heap)
            output.printstate()
            time.sleep(.10)
        else:
            break

        # else:
        #     print(stack[0])
        #     output.printfinalstate(sp, gp, stack)
        #     break
