class matrix_manipulation:
	def clock_spiral(matrix):
		""" 
		Going clockwise forming spiral in a matrix to create the order of values
		Parameter:
			k - starting row index 
			row - ending row index 
			l - starting column index 
			col - ending column index 
		"""
		row = len(matrix)    
		col = len(matrix[0])
		k = 0
		l = 0
		spiral = [] # Appending the order of values

		while (k<row and l<col):
			
			for i in range(l, col): 
				spiral.append(matrix[k][i]) 
					  
			k += 1   
			for i in range(k, row): 
				spiral.append(matrix[i][col-1])  
					  
			col -= 1 
			if ( k < row): 
					  
				for i in range(col - 1, (l - 1), -1):
					spiral.append(matrix[row - 1][i])  
				row -= 1
		 
			if (l < col): 
				for i in range(row - 1, k - 1, -1):
					spiral.append(matrix[i][l]) 
				l += 1

		return spiral


matrix = [
	[1,2,3],
	[8,9,4],
	[7,6,5]
]

spiral_matrix = matrix_manipulation.clock_spiral(matrix)
print(spiral_matrix)