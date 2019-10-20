class LuckyXor:
	def construct(self, a):
		lucky = '47'		
		for i in range(a+1, 101):
			num = str(a ^ i)
			count = 0
			for j in range(len(num)):
				if num[j] in lucky: count += 1
			if count == len(num): return i
		
		return -1