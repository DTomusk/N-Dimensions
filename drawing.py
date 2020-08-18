# all canvas tkinter stuff should go into this file 
from tkinter import *
from matrix import Matrix

canvas_width = 1600
canvas_height = 1200

ORIGIN=[canvas_width/2, canvas_height/2]
SCALE=80

def drawStuff(obj, canvas):
	canvas.delete("all")
	drawBG(canvas)
	drawObj(obj, canvas)

def drawBG(canvas):
	canvas.create_rectangle(0, 0, canvas_width, canvas_height, fill="black")

def drawObj(obj, canvas):
	coords = Matrix.conversion(obj.verts.row)*obj.verts
	for vec in coords.data:
		vec[0] *= SCALE
		vec[1] *= SCALE
		vec[0] += ORIGIN[0]
		vec[1] += ORIGIN[1]
		drawPoint(vec, canvas)
	for edge in obj.edges:
		drawLine(coords.data[edge[0]], coords.data[edge[1]], canvas)

def drawLine(start, end, canvas):
	color = "white"
	canvas.create_line(start[0], start[1],
		end[0], end[1], fill=color)

def drawPoint(point, canvas):
	canvas.create_rectangle(point[0]-2, point[1]-2, 
		point[0]+2, point[1]+2, fill="white")