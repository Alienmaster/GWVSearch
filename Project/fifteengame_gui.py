#!/usr/bin/python
import fifteengame
import inspect
from tkinter import *
from tkinter import messagebox


class gameUI():

	def __init__(self, state):

		self.state = state
		self.goalstate = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,'X']]
		self.buttons = []
		self.master = Tk()
		self.fifteenFrame = Frame(self.master)
		self.fifteenFrame.pack()
		self.functionsFrame = Frame(self.master, padx=20, pady=35)
		self.functionsFrame.pack()

		self.solveButton = Button(self.functionsFrame, text="Solve puzzle!")
		self.solveButton.grid(row=0, column=0, padx=5, pady=5)
		self.generateRandomButton = Button(self.functionsFrame, text="Generate new Puzzle!")
		self.generateRandomButton.grid(row=0, column=1, padx=5, pady=5)
		self.generateRandomButton.bind('<Button-1>', self.handleGenerateButton)
		self.resetButton = Button(self.functionsFrame, text="Reset")
		self.resetButton.grid(row=1, column=0, padx=5, pady=5)
		self.resetButton.bind('<Button-1>', self.handleReset)
		self.clearButton = Button(self.functionsFrame, text="Clear Moves")
		self.clearButton.grid(row=1, column=1, padx=5, pady=5)
		self.clearButton.bind('<Button-1>', self.handleClear)

		self.textFrame = Frame(self.master, pady=20)
		self.textFrame.pack()
		self.scrollbar = Scrollbar(self.textFrame)
		self.scrollbar.pack(side=RIGHT, fill=Y)
		self.listbox = Listbox(self.textFrame, height=5)
		self.listbox.pack()
		self.listbox.config(yscrollcommand=self.scrollbar.set)
		self.scrollbar.config(command=self.listbox.yview)

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
		self.listbox.delete(0, END)
		for i in self.l.returnMoves():
			self.listbox.insert(END, i)
		if (self.state == self.goalstate) and (not (str(inspect.stack()[1][3]) == "__init__") and (not (str(inspect.stack()[1][3]) == "handleReset"))):
			messagebox.showinfo("Done!", "The Puzzle has been solved!")

	def handleClear(self, event):
		self.l.resetMoves()
		self.loadState(self.state)

	def handleReset(self, event):
		self.state = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,'X']]
		self.l.resetMoves()
		self.loadState(self.state)

	def handleGenerateButton(self, event):
		self.state = self.l.generateRandomField()
		self.l.resetMoves()
		self.loadState(self.state)

	def handleSolveButton(self,event):
		self.state = self.l.astar(self.state)
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