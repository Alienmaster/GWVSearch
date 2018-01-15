#!/usr/bin/python

from tkinter import *
class gameUI():
	buttons = []

	def __init__(self, state):

		global buttons
		buttons = []
		master = Tk()
		C = Canvas(master, bg="blue", height=500, width=500)
		for x in range(0, len(state)):
			for y in range(0, len(state[x])):
				b = Button(master, text="", width=20, height=10)
				b.grid(row=x, column=y)
				buttons.append(b)
		self.loadState(state)


		master.mainloop()

	def loadState(self, state):
		c = 0
		for i in range(0, len(state)):
			for j in range(0, len(state[i])):
				global buttons
				buttons[c]["text"]=str(state[i][j])
				if state[i][j] == 'X':
					buttons[c].grid_remove()
				c += 1




g = gameUI([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,'X', 15]])