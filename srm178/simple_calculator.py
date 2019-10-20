class SimpleCalculator:
	def calculate(self, input):
		ops = ['-', '+', '/', '*']
		op = ''
		nums = []
		num = ''
		for i in range(len(input)):
			if input[i] in ops:
				op = input[i]
				nums.append(int(num))
				num = ''
			else: num += input[i]
		nums.append(int(num))
				
		return eval(str(nums[0]) + op + str(nums[1]))