from matrix import Matrix
from tkinter import *

root = Tk()
canvas_width = 1200
canvas_height = 800
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

def drawStuff():
	canvas.delete("all")
	drawBG()

def drawBG():
	canvas.create_rectangle(0, 0, canvas_width, canvas_height, fill="black")

def main():
	print("Enter number of dimensions")
	n = input()
	conversion = Matrix.conversion(n)
	print(conversion)

	A = Matrix([[5,1],[3,7]])
	B = Matrix([[6,6],[4,3]])
	print(A)
	print(B)
	print(A*B)

	I = Matrix.identity(5)
	print(I)

	print(Matrix.conversion(6)*Matrix.cube(6))

	drawStuff()
	mainloop()

if __name__=="__main__":
	main()