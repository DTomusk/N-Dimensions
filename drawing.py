# all canvas tkinter stuff should go into this file 
from tkinter import *
from matrix import Matrix
import math 

canvas_width = 1600
canvas_height = 1200

ORIGIN=[canvas_width/2, canvas_height/2]
SCALE=85

def drawStuff(obj, canvas):
	canvas.delete("all")
	drawBG(canvas)
	drawObj(obj, canvas)

def drawBG(canvas):
	canvas.create_rectangle(0, 0, canvas_width, canvas_height, fill="black")

def drawObj(obj, canvas):
	coords = convert(obj)
	for vec in coords.data:
		drawPoint(vec, canvas)
	for edge in obj.edges:
		drawLine(coords.data[edge[0]], coords.data[edge[1]], canvas)

def convert(obj):
	result = Matrix.conversion(obj.verts.row)*obj.verts
	for vec in result.data:
		vec[0] *= SCALE
		vec[1] *= SCALE
		vec[0] += ORIGIN[0]
		vec[1] += ORIGIN[1]
	return result

def drawLine(start, end, canvas):
	color = chooseColor(start, end)
	canvas.create_line(start[0], start[1],
		end[0], end[1], fill=color)

def chooseColor(start, end):
	mid = [(start[0]+end[0])/2, (start[1]+end[1])/2]
	distance = math.sqrt((mid[0]-ORIGIN[0])**2+(mid[1]-ORIGIN[1])**2)
	if distance < SCALE:
		return "#FFE8DD"
	elif distance < 2 * SCALE:
		return "#FFD2CD"
	elif distance < 3 * SCALE:
		return "#FFBCCA"
	elif distance < 3.5 * SCALE:
		return "#F4A9D3"
	else:
		return "#D59DE5"

def drawPoint(point, canvas):
	canvas.create_rectangle(point[0]-2, point[1]-2, 
		point[0]+2, point[1]+2, fill="white")

# don't know where to convert object from n dimensional to pixels 