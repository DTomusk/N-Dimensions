from matrix import Matrix

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

if __name__=="__main__":
	main()