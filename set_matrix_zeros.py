class matrix_manipulation:
	def set_zeros(matrix):
		"""
		Checks for zero in matrix and if present makes the row and col to be zeros
		"""
		row = len(matrix)
		col = len(matrix[0])
		indicator = False

		for i in range(row):

			if matrix[i][0] == 0:
				indicator = True

			for j in range(1, col):
				if matrix[i][j] == 0:
					matrix[0][j] = 0
					matrix[i][0] = 0

		for i in range(1, row):
				for j in range(1, col):
					if not matrix[0][j] or not matrix[i][0]:
						matrix[i][j] = 0

		if matrix[0][0] == 0:
			for j in range(col):
				matrix[0][j] = 0

		if indicator:
			for i in range(row):
				matrix[i][0] = 0

		return matrix


matrix = [
	[0,1,1],
	[1,1,1],
	[1,1,1]
]

result = matrix_manipulation.set_zeros(matrix)
print(result)