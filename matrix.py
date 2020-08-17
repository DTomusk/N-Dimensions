import math

class Matrix():
	def __init__(self, data):
		self.data = data

	def __str__(self):
		string = ""
		for x in self.data:
			for y in x:
				string += str(round(y,4)) + " "
			string += "\n"
		return string 

	@staticmethod
	def conversion(n):
		n = int(n)
		roots = []
		for i in range(n):
			angle = 2*(i/n)*math.pi
			roots.append([math.cos(angle),math.sin(angle)])
		return Matrix(roots)

