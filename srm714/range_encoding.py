class RangeEncoding:
	def minRanges(self, arr):
		count = 1
		if len(arr) == 1: return count
		for i in range(len(arr)-1):
			if arr[i] == arr[i+1] - 1: continue
			else: count += 1
	
		return count