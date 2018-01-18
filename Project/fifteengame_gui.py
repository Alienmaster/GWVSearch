#!/usr/bin/python
import fifteengame
from tkinter import *


class gameUI():

	def __init__(self, state):

		self.buttons = []
		self.master = Tk()
		self.fifteenFrame = Frame(self.master)
		self.fifteenFrame.pack()
		self.functionsFrame = Frame(self.master, padx=20, pady=35)
		self.functionsFrame.pack()
		self.solveButton = Button(self.functionsFrame, text="Solve puzzle!")
		self.solveButton.pack()

		self.loadState(state)


		self.master.mainloop()

	def loadState(self, state):
		c = 0
		for x in range(0, len(state)):
			for y in range(0, len(state[x])):
				b = Button(self.fifteenFrame, text="", width=20, height=10)
				b.grid(row=x, column=y)
				b.bind('<Button-1>', self.handleGameMove)
				self.buttons.append(b)
		for i in range(0, len(state)):
			for j in range(0, len(state[i])):
				self.buttons[c]["text"]=str(state[i][j])
				if state[i][j] == 'X':
					self.buttons[c].grid_remove()
				c += 1

	def handleGameMove(self, event):
		self.master.title('It works!')


l = fifteengame.gamelogic()
g = gameUI([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,'X', 15]])