from matrix import Matrix
from polytope import Poly
from tkinter import *
import math

import drawing

root = Tk()
canvas_width = 1600
canvas_height = 1200
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

ANGLE=math.pi/32

def moveStuff(poly, rotations):
	for rotation in rotations:
		poly.verts = rotation * poly.verts

def doStuff(poly, rotations):
	drawing.drawStuff(poly, canvas)
	moveStuff(poly, rotations)
	canvas.after(125, lambda: doStuff(poly, rotations))

def main():
	print("Enter number of dimensions")
	n = int(input())

	object = Matrix.cube(n)

	poly = Poly(n)

	rotations = []

	rotation = Matrix.identity(n)

	rotation.data[0][0] = math.cos(ANGLE)
	rotation.data[n-1][0] = math.sin(ANGLE)
	rotation.data[0][n-1] = -math.sin(ANGLE)
	rotation.data[n-1][n-1] = math.cos(ANGLE)

	rotations.append(rotation)

	doStuff(poly, rotations)
	mainloop()

if __name__=="__main__":
	main()