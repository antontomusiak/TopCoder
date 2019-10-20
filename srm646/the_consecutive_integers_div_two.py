class TheConsecutiveIntegersDivTwo:
	def find(self, numbers, k):
		if k == 1: return 0
		nums = sorted(list(numbers))
		diffs = [abs(nums[i] - nums[i-1]) for i in range(1, len(nums))]
		return min(diffs) - 1