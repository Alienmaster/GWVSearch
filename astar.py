import copy
import time
from heapq import heappush, heappop
import main
import output

def astar(sp, gp, tp1, tp2):
    """
    A* Suche
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
            if main.neighbourfree('u', x, y):
                arrow = main.direction('u', x, y)
                euklid = main.euklidischedistanz(arrow, gp)
                print(euklid)
                heappush(heap, (euklid, arrow[0], arrow[1]))
            if main.neighbourfree('r', x, y):
                arrow = main.direction('r', x, y)
                euklid = main.euklidischedistanz(arrow, gp)
                heappush(heap, (euklid, arrow[0], arrow[1]))
            if main.neighbourfree('d', x, y):
                arrow = main.direction('d', x, y)
                euklid = main.euklidischedistanz(arrow, gp)
                heappush(heap, (euklid, arrow[0], arrow[1]))
            if main.neighbourfree('l', x, y):
                arrow = main.direction('l', x, y)
                euklid = main.euklidischedistanz(arrow, gp)
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

    """
            if main.neighbourfree('u', x, y):
                arrow = main.direction('u', x, y)
                var_c = copy.deepcopy(stack[0])
                euklid = main.euklidischedistanz(sp, gp)
                var_c.append([arrow[0], arrow[1]])
                stack.append(var_c)
            if main.neighbourfree('r', x, y):
                arrow = main.direction('r', x, y)
                var_c = copy.deepcopy(stack[0])
                euklid = main.euklidischedistanz(sp, gp)
                var_c.append([arrow[0], arrow[1]])
                stack.append(var_c)
            if main.neighbourfree('d', x, y):
                arrow = main.direction('d', x, y)
                var_c = copy.deepcopy(stack[0])
                euklid = main.euklidischedistanz(sp, gp)
                var_c.append([arrow[0], arrow[1]])
                stack.append(var_c)
            if main.neighbourfree('d', x, y):
                arrow = main.direction('d', x, y)
                var_c = copy.deepcopy(stack[0])
                euklid = main.euklidischedistanz(sp, gp)
                var_c.append([arrow[0], arrow[1]])
                stack.append(var_c)
            stack.pop(0)
            x = stack[0][-1][0]
            y = stack[0][-1][1]
            output.printstate()
            print(x)
            print(y)
            i += 1
            """
        # else:
        #     print(stack[0])
        #     output.printfinalstate(sp, gp, stack)
        #     break
