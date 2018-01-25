# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 01:16:22 2018

@author: Marc
"""
import math
import sys

class PuzzleHeuristics:
    
    def getGoalCoordinates(self, matrix):
        goalCoords = []    
        for v in range(0, len(matrix)*len(matrix[0])):
            if v != 0:
                xGoal = (v - 1) % len(matrix)
                yGoal = math.floor((v - 1)/len(matrix))
                goalCoords.append((xGoal,yGoal))
        return goalCoords
    
    """Calutates the Manhatten Distance for the given puzzle
       as the sum of all distances from current position to goal position
       for each tile in the puzzle"""
    def calcMD(self, matrix):
        distance = 0
        goalCoords = self.getGoalCoordinates(matrix)
        for y in range(0, len(matrix)):
            for x in range(0, len(matrix[y])):
                if matrix[y][x] != 'X':
                    xGoal, yGoal = goalCoords[matrix[y][x] - 1]
                    distance += abs(x - xGoal) + abs(y - yGoal)            
        
        return distance
    
    """Calculates the Linear Conflict
       A linear conflict occurs when two tiles are in the same row or collumn
       as their goal position, but one or both tiles are blocked from reaching
       their goal by the other tile. In those cases, the distance will be increased
       by 2 for the two steps necessary for one tile to move out of the way."""
    def calcLC(self, matrix):
        distance = self.calcMD(matrix)
        goalCoords = self.getGoalCoordinates(matrix)
        for y in range(0, len(matrix)):
            for x in range(0, len(matrix)):
                if matrix[y][x] != 0:
                    xGoal, yGoal = goalCoords[matrix[y][x]-1]
                    """check for conflicts in row"""
                    if y == yGoal:
                        for i in range(1 + x, len(matrix[y])):
                            if (y == goalCoords[matrix[y][i]-1][1] and 
                                goalCoords[matrix[y][x]-1][0] > goalCoords[matrix[y][i]-1][0]):
                                distance += 2
                  
                    """check for conflicts in collumn"""
                    if x == xGoal:
                        for i in range(1 + y, len(matrix)):
                            if (x == goalCoords[matrix[i][x]-1][0] and
                                goalCoords[matrix[y][x]-1][1] > goalCoords[matrix[i][x]-1][1]):
                                distance += 2
        return distance
    
    #TODO: Alternative Heuristics
    
    def calcHeuristic(self, method, matrix):
        """
            Inputs
                method - chosen heuristic (MD = Manhatten Distance, LC = Linear Conflict)
                matrix - input matrix of puzzle
                
            Output
                heuristic value
        """    
        if method not in ('MD','LC'):
            sys.exit(1)
        
        if method == 'MD':
            return self.calcMD(matrix)
        if method == 'LC':
            return self.calcLC(matrix)