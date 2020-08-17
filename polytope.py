from matrix import Matrix

class Poly():
	def __init__(self, dim):
		self.verts = Matrix.cube(dim)
		nv = len(self.verts.data)
		self.edges = []
		for x in range(nv-1):
			for y in range(x, nv):
				if Poly.adjacent(self.verts.data[x], self.verts.data[y]):
					self.edges.append([x,y])

	def __str__(self):
		string = "Vertices:\n"
		for vert in self.verts.data:
			for coord in vert:
				string += str(coord) + " "
			string += "\n"
		string += "Edges:\n"
		for edge in self.edges:
			string += str(edge[0]) + " " + str(edge[1]) + "\n"
		return string

	@staticmethod
	def adjacent(a, b):
		number = 0
		for i in range(len(a)):
			if a[i] != b[i]:
				number += 1
		if number == 1:
			return True 
		else: 
			return False
