#!/usr/bin/python
import fifteengame
from tkinter import *


class gameUI():

	def __init__(self, state):

		self.state = state
		self.buttons = []
		self.master = Tk()
		self.fifteenFrame = Frame(self.master)
		self.fifteenFrame.pack()
		self.functionsFrame = Frame(self.master, padx=20, pady=35)
		self.functionsFrame.pack()
		self.solveButton = Button(self.functionsFrame, text="Solve puzzle!")
		self.solveButton.pack()
		self.generateRandomButton = Button(self.functionsFrame, text="Generate new Puzzle!")
		self.generateRandomButton.pack()
		self.generateRandomButton.bind('<Button-1>', self.handleGenerateButton)
		self.l = fifteengame.gamelogic()
		self.loadState(self.state)


		self.master.mainloop()

	def loadState(self, state):
		c = 0
		for widget in self.fifteenFrame.winfo_children():
			widget.destroy()
		self.fifteenFrame.update()
		self.buttons = []
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

	def handleGenerateButton(self, event):
		self.state = self.l.generateRandomField()
		self.loadState(self.state)

	def handleGameMove(self, event):
		c = 0
		for i in range(0, len(self.state)):
			for j in range(0, len(self.state[i])):
				if event.widget["text"] == str(self.state[i][j]):
					if j + 1 <= (len(self.state[i]))-1: 
						if self.state[i][j+1] == 'X':
							self.state = self.l.moveLeft(self.state)
							self.loadState(self.state)
							return
					if j - 1 >= 0:
						if self.state[i][j-1] == 'X':
							self.state = self.l.moveRight(self.state)
							self.loadState(self.state)
							return
					if i + 1 <= len(self.state)-1:
						if self.state[i+1][j] == 'X':
							self.state = self.l.moveUp(self.state)
							self.loadState(self.state)
							return
					if i - 1 >= 0:
						if self.state[i-1][j] == 'X':
							self.state = self.l.moveDown(self.state)
							self.loadState(self.state)
							return
				c += 1

g = gameUI([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,'X']])