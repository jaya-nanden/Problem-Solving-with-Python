
def rotate(A): 

    N = len(A[0])
    for i in range(N // 2): 
        for j in range(i, N - i - 1): 
            temp = A[i][j] 
            A[i][j] = A[N - 1 - j][i] 
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j] 
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i] 
            A[j][N - 1 - i] = temp 

    return A
    

matrix = [
	[1,2,6],
	[4,5,5],
	[4,5,5]
]


matrix_rotated = rotate(matrix)
print(matrix_rotated)
# print(len(matrix)


    # length = len(matrix[0])
    # temp = matrix[0][0]
    # matrix[0][0] = matrix[1][0]
    # matrix[1][0] = matrix[1][1]
    # matrix[1][1] = matrix[0][1]
    # matrix[0][1] = temp