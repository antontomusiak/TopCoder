class ForgetfulAddition:
	def minNumber(self, expression):
		exp = [x for x in expression]
		res = int(expression)
		for i in range(len(exp)-1):
			tmp = int(''.join(exp[:i+1])) + int(''.join(exp[i+1:]))
			res = min(res, tmp)
		return res