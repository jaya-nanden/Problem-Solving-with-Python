
matrix = [
			[1,2,3],
			[4,5,6]
			]

spiral = []


a = [
		[1,2,3],
		[4,5,6]
			]

# len(matrix)    --> no of rows
# len(matrix[0]) --> no of columns
row = len(a)    # 2
col = len(a[0]) # 3
k = 0
l = 0


while (k<row and l<col):
	''' k - starting row index 
		r - ending row index 
		l - starting column index 
		c - ending column index 
		i - iterator '''
	for i in range(l, col) : 
		print(a[k][i], end = " ")
		spiral.append(a[k][i]) 
			  
	k += 1   
	for i in range(k, row) : 
		print(a[i][col - 1], end = " ")
		spiral.append(a[i][col-1])  
			  
	col -= 1 
	if ( k < row) : 
			  
		for i in range(col - 1, (l - 1), -1) : 
			print(a[row - 1][i], end = " ") 
			spiral.append(a[row - 1][i])  
		row -= 1
 
	if (l < col) : 
		for i in range(row - 1, k - 1, -1) : 
			print(a[i][l], end = " ") 
			spiral.append(a[i][l]) 
		l += 1




		
# for i in range(0,len(matrix) - 1):
# 	for j in range(i,i+1):
# 		spiral.append(matrix[i][j])
# 		spiral.append(matrix[i][j+1])
# 		spiral.append(matrix[i+1][j+1])
# 		spiral.append(matrix[i+1][j])

print(spiral)