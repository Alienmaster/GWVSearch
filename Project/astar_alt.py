# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 22:31:51 2018

@author: Marc
"""
import sys
import puzzleheuristics as ph
import searchmoves as nm
from collections import deque
import numpy as np
import copy
from time import time
from heapq import heappop, heappush


class AStar:
    
    def __astar(self, heuristic, matrix):
        heu = ph.PuzzleHeuristics()
        move = nm.SearchMovements()
        visitedStates = []
        visitedStates.append(copy.deepcopy(matrix))
        heap = []
        heappush(heap, (heu.calcHeuristic('MD', matrix), matrix, []))
        while heap:
            pushList = []
            if move.isGoal(heap[0][1]):
                return heap[0]
            for a in move.getAdjacentCoordsEmpty(heap[0][1]):
                newState = move.moveStepByCoord(a, copy.deepcopy(heap[0][1]))
                if newState not in visitedStates:
                    element = (heu.calcHeuristic('MD', newState) + len(heap[0][2]), newState, heap[0][2] + [(a)])
                    pushList.append(element)
                    visitedStates.append(newState)
            heappop(heap)
            while pushList:
                heappush(heap, pushList.pop(0))
        return "No result found"
    
    def search(self, matrix, heuristic):
              
        for x in range(0, len(matrix)):
            for y in range(0, len(matrix[x])):
                if matrix[x][y] not in (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15):
                    matrix[x][y] = 0
             
        return self.__astar(heuristic, matrix)
    

testmatrix = [[5,3,11,4],
                [9,1,8,10],
                [6,2,0,12],
                [7,15,13,14]]
testmatrix2 = [[10, 2, 0, 3],
         [1,4,7,11],
         [13,9,14,12],
         [15,5,8,6]]
testmatrix3 = [[10, 0, 2, 3],
         [1,4,7,11],
         [13,9,14,12],
         [15,5,8,6]]
goalstate = [[5,1,3,4],
             [0,2,7,8],
             [9,6,10,12],
             [13,14,11,15]]


a = AStar()
t1 = time()
print(a.search(testmatrix, 'LC'))
print(time()-t1)