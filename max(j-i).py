class Maxdiff:
	def max_diff_indexes(arr):
		"""
		Along with conditions to find which difference of indexes are maximum
		Conditions:
			j > i
			arr[j] > arr[i]
		"""
		diff = -1
		n = len(arr)
		for i in range(0, n): 
		    j = n - 1
		    while(j > i): 
		        if arr[j] > arr[i] and (j - i) > diff: 
		            diff = j - i
		            print(diff) 
		            print(arr[j], arr[i])
		        j -= 1

		return diff


arr = [1, 4, 6, 40, 5, 35, 1]

result = Maxdiff.max_diff_indexes(arr)
print(result)

