# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 02:41:55 2018

@author: Marc
"""

import numpy as np
#from collections import deque

class SearchMovements:
    
    def __init__(self):
        self.goal = np.array([[1,2,3,4],
                              [5,6,7,8],
                              [9,10,11,12],
                              [13,14,15,0]])
    
    def isGoal(self, matrix):
        matrixA = np.copy(matrix)
        if (matrixA==self.goal).all():
            return True
        return False
    
    def getEmptyTile(self, matrix):
        emptyTile = []
        for x in range(0, len(matrix)):
            for y in range(0, len(matrix[x])):
                if matrix[x][y] == 0:
                    emptyTile = (x,y)
        return emptyTile
    
    def getAdjacentCoordsEmpty(self, matrix):
        adjCoords = []
        (x,y) = self.getEmptyTile(matrix)
        movements = ((x-1,y),(x+1,y),(x,y-1),(x,y+1))
        for m in movements:
            if m[0] < 0 or m[1] < 0:
                continue
            if m[0] > len(matrix)-1 or m[1] > len(matrix)-1:
                continue
            adjCoords.append(m)
        return adjCoords
                
        return matrix
    
    def moveStepByCoord(self, step, matrix):
        if step not in self.getAdjacentCoordsEmpty(matrix):
            raise ValueError('Coordinates not adjacent to empty tile in matrix!')
        e = self.getEmptyTile(matrix)
        matrix[e[0]][e[1]] = matrix[step[0]][step[1]]
        matrix[step[0]][step[1]] = 0
        return matrix
 


