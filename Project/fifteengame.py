import puzzleheuristics
from random import *

class gamelogic():

	def __init__(self):
		self.h = puzzleheuristics.PuzzleHeuristics()
		self.Moves = []
		self.goalState = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,'X']]

	def generateRandomField(self):
		state = self.goalState
		for i in range(0, 100):
			t = randint(1, 4)
			if t == 1:
				state = self.moveLeft(state)
			elif t == 2:
				state = self.moveRight(state)
			elif t == 3:
				state = self.moveUp(state)
			elif t == 4:
				state = self.moveDown(state)
		if not self.isValidState(state):
			state = self.generateRandomField()		
		return state

	def isValidState(self, state):
		liststate = []
		integrityCounter = 0

		#convert field to list for calculations and calculates vertical displacement parity
		for i in range(0, len(state)):
			for j in state[i]:
				if j == 'X':
					integrityCounter += i+1
				else:
					liststate.append(j)

		# calculates horizontal displacement parity
		for i in range(0, len(liststate)):
			if not liststate[i] == liststate[0]:
				for j in range(0, i-1):
					if liststate[j] > liststate[i]:
						integrityCounter += 1

		#returns if the state is valid (parity can be divided by 2)
		if integrityCounter % 2 == 0:
			return True
		else:
			return False

	def returnMoves(self):
		return self.Moves

	def resetMoves(self):
		self.Moves = []

	def returnPossibleMoves(self, state):
		possible=[]
		for i in range(0, len(state)):
			for j in range(0, len(state[i])):
				if state[i][j] == 'X':
					if j > 0:
						possible.append('L')
					if j < len(state[i])-1:
						possible.append('R')
					if i > 0:
						possible.append('U')
					if i < len(state)-1:
						possible.append('D')
		return possible

	def astar(self, state):
		path = [state]
		node = state

		return
		#TODO


	def moveLeft(self, state):
		Input = state
		d = False
		self.Moves.append("L")
		for i in range(0, len(Input)):
			for j in range(0,len(Input[i])):
				if Input[i][j] == 'X':
					t = Input[i][j-1]
					Input[i][j-1] = 'X'
					Input[i][j] = t
					break
		return Input

	def moveRight(self, state):
		Input = state
		self.Moves.append("R")
		for i in range(0, len(Input)):
			for j in range(0,len(Input[i])-1):
				if Input[i][j] == 'X':
					t = Input[i][j+1]
					Input[i][j+1] = 'X'
					Input[i][j] = t
					break
		return Input

	def moveUp(self, state):
		Input = state
		self.Moves.append("U")
		for i in range(0, len(Input)):
			for j in range(0,len(Input[i])):
				if Input[i][j] == 'X':
					t = Input[i-1][j]
					Input[i-1][j] = 'X'
					Input[i][j] = t
					break
		return Input

	def moveDown(self, state):
		Input = state
		d = False
		self.Moves.append("D")
		for i in range(0, len(Input)-1):
			for j in range(0,len(Input[i])):
				if Input[i][j] == 'X':
					t = Input[i+1][j]
					Input[i+1][j] = 'X'
					Input[i][j] = t
					d = True
					break
			if d == True:
				break
		return Input
