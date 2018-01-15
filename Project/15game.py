Input = [[],[],[],[]]
#Goal = [[1,2,3,4][5,6,7,8][9,10,11,12][13,14,15,X]]
Moves = []



def movePossible():
	#TODO
	return True


def moveLeft():
	global Input, Moves
	Moves.append("L")
	if movePossible():
		for i in range(0, len(Input)-1):
			for j in range(0,len(Input[i])-1):
				if Input[i][j] == 'X':
					t = Input[i][j-1]
					Input[i][j-1] = 'X'
					Input[i][j] = t
					return

def moveRight():
	global Input, Moves
	Moves.append("R")
	if movePossible():
		for i in range(0, len(Input)-1):
			for j in range(0,len(Input[i])-1):
				if Input[i][j] == 'X':
					t = Input[i][j+1]
					Input[i][j+1] = 'X'
					Input[i][j] = t
					return

def moveUp():
	global Input, Moves
	Moves.append("U")
	if movePossible():
		for i in range(0, len(Input)-1):
			for j in range(0,len(Input[i])-1):
				if Input[i][j] == 'X':
					t = Input[i-1][j]
					Input[i-1][j] = 'X'
					Input[i][j] = t
					return

def moveDown():
	global Input, Moves
	Moves.append("D")
	if movePossible():
		for i in range(0, len(Input)-1):
			for j in range(0,len(Input[i])-1):
				if Input[i][j] == 'X':
					t = Input[i+1][j]
					Input[i+1][j] = 'X'
					Input[i][j] = t
					return

Input = [	[1,'X',3,4],
			[5,2,7,8],
			[9,6,11,12],
			[13,10,14,15]]

moveDown()
print(Input)
moveUp()
print(Input)
print(Moves)

