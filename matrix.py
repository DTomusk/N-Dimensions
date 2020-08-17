import math

class Matrix():
	def __init__(self, data):
		self.data = data
		self.col = len(data)
		self.row = len(data[0])

	def __str__(self):
		string = ""
		for i in range(self.row):
			for j in range(self.col):
				string += str(round(self.data[j][i])) + " "
			string += "\n"
		return string 

	def __mul__(self, other):
		if self.col != other.row:
			return 0
		result = Matrix.zeros([self.row, other.col])
		for i in range(self.row):
				for j in range(other.col):
					for k in range(self.col):
						result.data[j][i] += self.data[k][i]*other.data[j][k]
		return result

	@staticmethod
	def zeros(dim):
		matrix = []
		for j in range(dim[1]):
			matrix.append([])
			for i in range(dim[0]):
				matrix[j].append(0)
		return Matrix(matrix)

	@staticmethod
	def identity(n):
		matrix = Matrix.zeros([n,n])
		for i in range(n):
			matrix.data[i][i] = 1
		return matrix 

	@staticmethod
	def conversion(n):
		n = int(n)
		roots = []
		for i in range(n):
			angle = 2*(i/n)*math.pi
			roots.append([math.cos(angle),math.sin(angle)])
		return Matrix(roots)

