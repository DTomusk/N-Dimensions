from matrix import Matrix
from polytope import Poly, Eeight
from tkinter import *
import math

import drawing

root = Tk()
canvas_width = 1600
canvas_height = 1200
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

ANGLE=math.pi/32

def moveStuff(poly, r):
	for x in r:
		poly.verts = poly.rotations[x] * poly.verts

def doStuff(poly, r):
	drawing.drawStuff(poly, canvas)
	#moveStuff(poly, r)
	#canvas.after(125, lambda: doStuff(poly, r))

def main():
	print("Enter number of dimensions")
	n = int(input())

	poly = Poly(n)

	eee = Eeight()
	print(eee)

	r = [1,4,8]

	doStuff(eee, r)
	mainloop()

if __name__=="__main__":
	main()