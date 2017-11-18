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
    heap = []
    heappush(heap, (gp[0]-x+gp[1]-y,0, x, y, [[x,y]]))
    while True:
        if main.goalnotreached(x, y):
            main.setmarker(x, y)
            topush = []
            if(main.neighbourfree('u', x, y)):
                euklid = gp[0] - (x-1) + (gp[1] - y)
                u = (heap[0][1]+euklid,heap[0][1]+1, x-1, y, heap[0][4]+[[x-1, y]])
                topush.append(u)
            if(main.neighbourfree('r', x, y)):
                euklid = gp[0] - x + (gp[1] - (y+1))
                r = (heap[0][1]+euklid,heap[0][1]+1, x, y+1, heap[0][4]+[[x, y+1]])
                topush.append(r)
            if(main.neighbourfree('d', x, y)):
                euklid = gp[0] - (x+1) + (gp[1] - y)
                d = (heap[0][1]+euklid,heap[0][1]+1, x+1, y, heap[0][4]+[[x+1, y]])
                topush.append(d)
            if(main.neighbourfree('l', x, y)):
                euklid = gp[0] - x + (gp[1] - (y-1))
                l = (heap[0][1]+euklid,heap[0][1]+1, x, y-1, heap[0][4]+[[x, y-1]])
                topush.append(l)
            heappop(heap)
            while not len(topush) == 0:
                heappush(heap, topush[0])
                topush.pop(0)
            #print(heap)
            x = heap[0][2]
            y = heap[0][3]
            output.printstate()
            #time.sleep(.10)
        else:
            print(heap[0][4])
            break

        # else:
        #     print(stack[0])
        #     output.printfinalstate(sp, gp, stack)
        #     break
