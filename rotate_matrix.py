class matrix_manipulation:
    def rotate(matrix): 
        """
        Takes matrix and rotates 90 degree clockwise
        """
        N = len(matrix[0])
        for i in range(N // 2): 
            for j in range(i, N - i - 1): 
                temp = matrix[i][j] 
                matrix[i][j] = matrix[N - 1 - j][i] 
                matrix[N - 1 - j][i] = matrix[N - 1 - i][N - 1 - j] 
                matrix[N - 1 - i][N - 1 - j] = matrix[j][N - 1 - i] 
                matrix[j][N - 1 - i] = temp 

        return matrix
    

matrix = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]

result =  matrix_manipulation.rotate(matrix)
print(result)
