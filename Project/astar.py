# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 22:31:51 2018

@author: Marc
"""
import sys
import puzzleheuristics
import searchmovements
from collections import deque
import numpy as np

class AStar:
    
    def __init__(self):
        self.matrix = []
    
    def __astar(self, heuristic):
        heu = puzzleheuristics.PuzzleHeuristics()
        move = searchmovements.SearchMovements(self.matrix)
        """get adjacent coordinates"""
        lastStep = move.getEmptyTile()
        adjCoords = move.getAdjacentCoordsEmpty()
        frontier = deque()
        for f in adjCoords:
            frontier.append([f])
            
        counter = 0
        while frontier:
            counter += 1
            path = []
            if move.isGoal():
                return path
            hValue = sys.maxsize
            for f in frontier:
                """go to next search state"""
                move.movementBySequenceCoords(f)
                move.reverseLastSequence()
                """calculate fValue throughout all paths on the frontier"""
                fcValue = len(f) + heu.calcHeuristic(heuristic, self.matrix)
                if fcValue < hValue:
                    hValue = fcValue
                    path = f
                if len(path) > 1:
                    lastStep = path[-2]
                    
            print("[",counter,"]: Current Path: ", path, ", with length: ", len(path))
            print("Current HVALUE", hValue)
            move.movementBySequenceCoords(path)
            if move.isGoal():
                return path
            adjCoords = move.getAdjacentCoordsEmpty()
            adjCoords.remove(lastStep)
            move.reverseLastSequence()
            frontier.remove(path)
            for c in adjCoords:
                frontier.append(path + [c])
        return 0
    
    def search(self, matrix, heuristic):
        for x in range(0, len(matrix)):
            for y in range(0, len(matrix[x])):
                if matrix[x][y] not in (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15):
                    matrix[x][y] = 0
        self.matrix = matrix
        self.__astar(heuristic)
        
        return 0
    

testmatrix = [[7,2,15,12],
              [11,13,0,8],
              [1,4,6,3],
              [14,5,10,9]]
testmatrix2 = [[7,15,2,12],
              [11,0,13,8],
              [1,4,3,6],
              [14,5,10,9]]
goalMatrix = [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,0]]

a = AStar()
b = a.search(testmatrix, 'LC')
print(b)

"""
a = np.matrix(testmatrix)
b = np.matrix(testmatrix2)
x = (a,8)
y = (b,9)

f = deque()
f.append(x)
f.append(y)
heu = puzzleheuristics.PuzzleHeuristics()
foo = heu.calcHeuristic('LC', a)
print(foo)
"""