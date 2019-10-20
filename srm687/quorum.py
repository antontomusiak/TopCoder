class Quorum:
	def count(self, arr, k):
        return sum(sorted(arr)[:k])
