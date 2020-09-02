class Duplicate:
	def no_duplicate(arr):
		""" 
		Input list of unique and repeated numbers
		Output list of unique numbers
			arr - list
		"""
		return list(set(arr))

	def no_duplicate_without_set(arr):

		length = len(arr)

		if length == 0 or length == 1:
			return arr

		temp = list(range(length))
		j = 0
		for i in range(0, length-1):
			if (arr[i] != arr[i+1]):
				temp[j] = arr[i]
				j += 1

		temp[j] = arr[length-1]
		j += 1
		for i in range(0, j): 
			arr[i] = temp[i] 
		return j


arr = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7]

new_arr= Duplicate.no_duplicate(arr)
# Using set datastructure in python
# print('No duplicates {}'.format(new_arr))

new_arr_len = Duplicate.no_duplicate_without_set(arr)

print('No duplicates {}'.format(arr[:new_arr_len]))

	
