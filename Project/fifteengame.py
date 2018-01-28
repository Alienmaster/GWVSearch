import puzzleheuristics
from heapq import heappush, heappop
from random import *
import time
import copy
class gamelogic():

	def __init__(self):
		self.h = puzzleheuristics.PuzzleHeuristics()
		self.Moves = []
		self.goalState = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]

	def generateRandomField(self):
		state = copy.deepcopy(self.goalState)
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
				if j == 0:
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
				if state[i][j] == 0:
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
		visitedStates = []
		visitedStates.append(copy.deepcopy(state))
		#Elements in heap: (Cost, Current State, Path taken(nodes), Path taken(moves) )
		heap = []
		heappush(heap, (self.h.calcMD(state), state, [state], []))
		while not heap == []:
			topush = []
			print(heap[0][1])
			time.sleep(.10)
			if heap[0][1] == self.goalState:
				return heap[0]
				break
			for i in self.returnPossibleMoves(heap[0][1]):
				if i == 'U':
					t1 = self.moveUp(copy.deepcopy(heap[0][1]))
					print('u' + str(t1))
					if not t1 in heap[0][3]:
						u = (self.h.calcMD(t1)+1, t1, heap[0][2]+[t1], heap[0][3]+['U'])
						topush.append(u)
				if i == 'D':
					t2 = self.moveDown(copy.deepcopy(heap[0][1]))
					print('d'+ str(t2))
					if not t2 in heap[0][3]:
						d = (self.h.calcMD(t2)+1, t2, heap[0][2]+[t2], heap[0][3]+['D'])
						topush.append(d)
				if i == 'L':
					t3 = self.moveLeft(copy.deepcopy(heap[0][1]))
					print('l' + str(t3))
					if not t3 in heap[0][3]:
						l = (self.h.calcMD(t3)+1, t3, heap[0][2]+[t3], heap[0][3]+['L'])
						topush.append(l)
				if i == 'R':
					t4 = self.moveRight(copy.deepcopy(heap[0][1]))
					print('r'+str(t4))
					if not t4 in heap[0][3]:
						r = (self.h.calcMD(t4)+1, t4, heap[0][2]+[t4], heap[0][3]+['R'])
						topush.append(r)
			heappop(heap)
			while not len(topush) == 0:
				heappush(heap, topush[0])
				topush.pop(0)
			#print("heap "+str(heap))
		print("Something went wrong!")
		return
		#TODO


	def moveLeft(self, state):
		Input = state
		d = False
		self.Moves.append("L")
		for i in range(0, len(Input)):
			for j in range(0,len(Input[i])):
				if Input[i][j] == 0:
					t = Input[i][j-1]
					Input[i][j-1] = 0
					Input[i][j] = t
					break
		return Input

	def moveRight(self, state):
		Input = state
		self.Moves.append("R")
		for i in range(0, len(Input)):
			for j in range(0,len(Input[i])-1):
				if Input[i][j] == 0:
					t = Input[i][j+1]
					Input[i][j+1] = 0
					Input[i][j] = t
					break
		return Input

	def moveUp(self, state):
		Input = state
		self.Moves.append("U")
		for i in range(0, len(Input)):
			for j in range(0,len(Input[i])):
				if Input[i][j] == 0:
					t = Input[i-1][j]
					Input[i-1][j] = 0
					Input[i][j] = t
					break
		return Input

	def moveDown(self, state):
		Input = state
		d = False
		self.Moves.append("D")
		for i in range(0, len(Input)-1):
			for j in range(0,len(Input[i])):
				if Input[i][j] == 0:
					t = Input[i+1][j]
					Input[i+1][j] = 0
					Input[i][j] = t
					d = True
					break
			if d == True:
				break
		return Input
