# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 23:27:31 2018

@author: Marc
"""
import sys
from collections import deque
import searchmoves as sm
import copy
import pickle


class PatternDatabase:

    def __init__(self):
        self.IDList = []
        self.path = []
    
    def getId(self, matrix):
        ident = ''
        for m in matrix:
            for n in m:
                if n == -1:
                    n = '_'
                ident += str(n) + '/'
        return ident
    
    def storeDatabase(self, filename, db):
        dic = {}
        for d in db:
            dic[self.getId(d[0])] = d[1]
        
        with open(filename, 'wb') as handle:
            pickle.dump(dic, handle, protocol=pickle.HIGHEST_PROTOCOL)

        with open(filename, 'rb') as handle:
            b = pickle.load(handle)
            
        print("CHECK: \n", b)
        
        return dic == b
    
    def getPatternList(self, state, patternType):
        patternList = []
        matrixList = []
        
        if len(state) == 4:
            if patternType == 'fringe':
                patternA = [1,2,3,4,5,9,13]
                patternB = [6,7,8,10,11,12,14,15]
                patternList = (patternA, patternB)
        if len(state) == 3:
            if patternType == 'fringe':
                patternA = [1,2,3,4,7]
                patternB = [5,6,8]
                patternList = (patternA, patternB)
        if len(state) == 2:
            if patternType == 'fringe':
                patternA = [1,2]
                patternB = [3]
                patternList = (patternA, patternB)
        
        for p in patternList:
            matrix = copy.deepcopy(state)
            for x in range(len(state)):
                for y in range(len(state[x])):
                    if state[x][y] == 0:
                        matrix[x][y] = 0
                    elif state[x][y] not in p:
                        matrix[x][y] = -1
                    elif state[x][y] in p:
                        matrix[x][y] = state[x][y]
            matrixList.append(matrix)
        
        return matrixList
    
    def searchPermutations(self, matrix):
        move = sm.SearchMovements()
        patternList = self.getPatternList(matrix, 'fringe')
        frontier = deque()
        visited = []
        counter = 0
        for p in patternList:
            frontier.append((p,0))
            visited.append((copy.deepcopy(p), 0))
            while frontier:
                counter += 1
                #print(counter)
                tup = frontier.popleft()
                state = tup[0]
                steps = tup[1]
                adjCoords = move.getAdjacentCoordsEmpty(state)
                for a in adjCoords:
                    newState = move.moveStepByCoord(a, copy.deepcopy(state))
                    if not any((newState == x[0]) for x in visited):
                        frontier.append((newState, steps+1))
                        visited.append((newState, steps+1))
        
        return visited
       
    def createDatabase(self, matrix, patternType):
        result = []
        if patternType not in ('fringe', 'corner'):
            print('Wrong argument for Pattern Database')
            sys.exit(1)
        if patternType == 'fringe':
            result = self.getPatternList(matrix,'fringe')
        if patternType == 'corner':
            result = 0
        return result
        
patternA = [[1,2,3,4],
            [5,-1,-1,-1],
            [9,-1,-1,-1],
            [13,-1,-1,0]]

patternB = [(-1,-1,-1,-1),(-1,6,7,8),(-1,10,11,12),(-1,14,15,0)]

testmatrix = [[2,3,5,1],
              [10,12,15,6],
              [7,8,9,11],
              [14,13,4,0]]
testmatrix2 = [[1,2,3],
               [4,5,6],
               [7,8,0]]
testmatrix3 = [[1,2],
               [3,0]]

s = PatternDatabase()

#print(s.getPatternList(testmatrix3, 'fringe'))

perm = (s.searchPermutations(testmatrix3))
"""
i = 0
for p in perm:
    print("M: ", i, " \n", s.getId(p[0]))
    i += 1
print("test: ", len(perm))
"""
print(s.storeDatabase('testfile', perm))
