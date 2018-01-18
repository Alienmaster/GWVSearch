class gamelogic():

	def __init__(self):
		self.Moves = []

	def returnMovesAsString():
		#TODO
		return

	def movePossible(input, direction):
		#TODO
		return True


	def moveLeft(self, state):
		Input = state
		d = False
		self.Moves.append("L")
		#if movePossible():
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
		#if movePossible():
		for i in range(0, len(Input)):
			for j in range(0,len(Input[i])-1):
				if Input[i][j] == 'X':
					print(Input)
					t = Input[i][j+1]
					Input[i][j+1] = 'X'
					Input[i][j] = t
					break
		return Input

	def moveUp(self, state):
		Input = state
		self.Moves.append("U")
		#if movePossible():
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
		#if movePossible():
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
