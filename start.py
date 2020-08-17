from matrix import Matrix

def main():
	print("Enter number of dimensions")
	n = input()
	conversion = Matrix.conversion(n)
	print(conversion)

if __name__=="__main__":
	main()