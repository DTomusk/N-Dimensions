from matrix import Matrix
import math, random

class Poly():
	def __init__(self, dim):
		self.verts = Matrix.cube(dim)
		nv = len(self.verts.data)
		self.edges = []
		for x in range(nv-1):
			for y in range(x, nv):
				if Poly.adjacent(self.verts.data[x], self.verts.data[y]):
					self.edges.append([x,y])
		# rotations stores all rotation matrices 
		self.rotations = []
		for x in range(dim-1):
			for y in range(x+1, dim):
				angle = math.pi/(random.randrange(49)+30)
				print(angle)
				rotation = Matrix.identity(dim)
				rotation.data[x][x] = math.cos(angle)
				rotation.data[x][y] = math.sin(angle)
				rotation.data[y][x] = -math.sin(angle)
				rotation.data[y][y] = math.cos(angle)
				self.rotations.append(rotation)

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

class Eeight(Poly):
	def __init__(self):
		self.verts = Eeight.verts()
		nv = 241
		self.edges = []
		for x in range(nv-1):
			for y in range(x, nv):
				if Poly.adjacent(self.verts.data[x], self.verts.data[y]):
					self.edges.append([x,y])

	def verts():
		verts = Matrix.cube(8)
		for vert in verts.data:
			if sum(vert) % 4 != 0:
				verts.data.remove(vert)
		for x in range(7):
			for y in range(x+1, 8):
				new = [0,0,0,0,0,0,0,0]
				new[x] = 2
				new[y] = 2
				verts.data.append(new)
				new = [0,0,0,0,0,0,0,0]
				new[x] = -2
				new[y] = 2
				verts.data.append(new)
				new = [0,0,0,0,0,0,0,0]
				new[x] = 2
				new[y] = -2
				verts.data.append(new)
				new = [0,0,0,0,0,0,0,0]
				new[x] = -2
				new[y] = -2
				verts.data.append(new)
		return verts



