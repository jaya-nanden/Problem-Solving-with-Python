
# Set the whole row to be zero if there is zero in it

print('----------------')
print('\n Ready to go!	\n')
print('----------------')


a = [
		[0,1,1],
		[0,1,1],
		[1,1,1]
]

print(a)
row = len(a)
col = len(a[0])
k = set()
l = set()
print('Row --> ', row)
print('Column --> ', col)

indicator = False

for i in range(row):

	if a[i][0] == 0:
		indicator = True

	for j in range(1, col):
		if a[i][j] == 0:
			a[0][j] = 0
			a[i][0] = 0

for i in range(1, row):
		for j in range(1, col):
			if not a[0][j] or not a[i][0]:
				a[i][j] = 0

# First row
if a[0][0] == 0:
	for j in range(col):
		a[0][j] = 0

# First col
if indicator:
	for i in range(row):
		a[i][0] = 0

print(a)
print('indicator --> ', indicator)

'''
above Algo : Intuition
Time Complexity : O(M times N)O(M×N)
Space Complexity : O(1)O(1)
'''




'''Algo 1 '''

# for i in range(row):
# 	for j in range(col):
# 		if a[i][j] == 0:
# 			k.add(i)
# 			l.add(j)

# for i in range(row):
# 	for j in range(col):
# 		if i in k or j in l:
# 			a[i][j] = 0


# print(a)
