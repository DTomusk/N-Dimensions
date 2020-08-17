from matrix import Matrix
from polytope import Poly
from tkinter import *
import math

root = Tk()
canvas_width = 1600
canvas_height = 1200
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

ORIGIN=[canvas_width/2, canvas_height/2]
SCALE=80
ANGLE=math.pi/24

def drawStuff(obj):
	canvas.delete("all")
	drawBG()
	drawObj(obj)

def drawBG():
	canvas.create_rectangle(0, 0, canvas_width, canvas_height, fill="black")

def drawObj(obj):
	coords = Matrix.conversion(obj.verts.row)*obj.verts
	for vec in coords.data:
		vec[0] *= SCALE
		vec[1] *= SCALE
		vec[0] += ORIGIN[0]
		vec[1] += ORIGIN[1]
		drawPoint(vec)
	print(coords)
	for edge in obj.edges:
		drawLine(coords.data[edge[0]], coords.data[edge[1]])

def drawLine(start, end):
	print(start)
	print(end)
	canvas.create_line(start[0], start[1],
		end[0], end[1], fill="white")

def drawPoint(point):
	canvas.create_rectangle(point[0]-2, point[1]-2, 
		point[0]+2, point[1]+2, fill="white")

def moveStuff(poly, rotation):
	poly.verts = rotation * poly.verts

def doStuff(poly, rotation):
	drawStuff(poly)
	#moveStuff(poly, rotation)
	#canvas.after(100, lambda: doStuff(poly, rotation))

def main():
	print("Enter number of dimensions")
	n = int(input())

	object = Matrix.cube(n)

	poly = Poly(n)
	print(poly)

	rotation = Matrix.identity(n)
	rotation.data[0][0] = math.cos(ANGLE)
	rotation.data[1][0] = math.sin(ANGLE)
	rotation.data[0][1] = -math.sin(ANGLE)
	rotation.data[1][1] = math.cos(ANGLE)

	doStuff(poly, rotation)
	mainloop()

if __name__=="__main__":
	main()