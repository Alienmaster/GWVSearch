# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 19:43:24 2018

@author: Marc
"""

class SearchMovements:
    
    def __init__(self, matrix):
        self.lastEmptyTile = []
        self.lastSequence = []
        self.matrix = matrix
    
    def isGoal(self):
        goalMatrix = [[1,2,3,4],
                      [5,6,7,8],
                      [9,10,11,12],
                      [13,14,15,0]]
        for x in range(0,len(self.matrix)):
            for y in range(0,len(self.matrix[x])):
                if self.matrix[x][y] != goalMatrix[x][y]:
                    return False
        return True
    
    
    """Get coordinates of empty tile within a matrix"""
    def getEmptyTile(self):
        emptyTile = []
        for x in range(0, len(self.matrix)):
            for y in range(0, len(self.matrix[x])):
                if self.matrix[x][y] == 0:
                    emptyTile = (x,y)
                    
        return emptyTile
    
    """Get coordinates of a specific tile within the matrix"""
    def getTileCoords(self, tile):
        for x in range(0, len(self.matrix)):
            for y in range(0, len(self.matrix[x])):
                if tile == self.matrix[x][y]:
                    return (x,y)
                
    def getTileValue(self, coords):
        return self.matrix[coords[0]][coords[1]]
    
    def getAdjacentEmpty(self):
        adj = []
        (x,y) = self.getEmptyTile()
        movements = ((x-1,y),(x+1,y),(x,y-1),(x,y+1))
        for m in movements:
            if m[0] < 0 or m[1] < 0:
                continue
            try:
                adj.append(self.matrix[m[0]][m[1]])
            except IndexError:
                continue
        return adj
    
    def getAdjacentCoordsEmpty(self):
        adjCoords = []
        (x,y) = self.getEmptyTile()
        movements = ((x-1,y),(x+1,y),(x,y-1),(x,y+1))
        for m in movements:
            if m[0] < 0 or m[1] < 0:
                continue
            if m[0] > len(self.matrix)-1 or m[1] > len(self.matrix)-1:
                continue
            adjCoords.append(m)
        return adjCoords
    
    def getAdjacentToCoords(self, coords):
        adj = []
        (x,y) = coords
        movements = ((x-1,y),(x+1,y),(x,y-1),(x,y+1))
        for m in movements:
            if m[0] < 0 or m[1] < 0:
                continue
            try:
                adj.append(self.matrix[m[0]][m[1]])
            except IndexError:
                continue
        
        return adj

    """Not save to use; use movementBySequence instead"""
    def __moveTileByCoords(self, coords):
        adjCoords = self.getAdjacentCoordsEmpty()
        if coords == self.getEmptyTile():
            return self.matrix
        if coords in adjCoords:
            empty = self.getEmptyTile()
            self.matrix[empty[0]][empty[1]] = self.getTileValue(coords)
            self.matrix[coords[0]][coords[1]] = 0
        else:
            raise ValueError('tile not adjacent to empty tile!')
        return self.matrix
    
    def movementBySequenceCoords(self, seq):
        self.lastEmptyTile = self.getEmptyTile()
        self.lastSequence = seq
        for s in seq:
            self.__moveTileByCoords(s)
        return self.matrix
    
    def reverseLastSequence(self):
        for s in reversed(self.lastSequence):
            if s == self.getEmptyTile():
                continue
            self.__moveTileByCoords(s)
        self.__moveTileByCoords(self.lastEmptyTile)
        return self.matrix
    """
testmatrix = [[2,3,5,1],
              [10,12,15,6],
              [7,8,9,11],
              [14,13,4,0]]

testmatrix2 = [[13,3,5,1],
              [10,12,15,6],
              [7,8,9,11],
              [2,14,4,0]]

goalMatrix = [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,0]]

s = SearchMovements(testmatrix)
foo = s.movementBySequenceCoords([(2, 3), (1, 3), (0, 3)])
print("1",foo)
foo = s.reverseLastSequence()
print("1",foo)
s = SearchMovements(goalMatrix)
print(s.getAdjacentCoordsEmpty())

print(s.isGoal())
"""