def op(a, b, c):
	if b == '-': return int(a) - int(c)
	elif b == '+': return int(a) + int(c)
	elif b == '*': return int(a) * int(c)
	else: return int(a) / int(c)	

class NoOrderOfOperations:
	def evaluate(self, expr):
		if len(expr) == 0: return int(expr)
		expr = list(expr)
		for i in range(2, len(expr), 2):
			expr[i] = op(expr[i-2], expr[i-1], expr[i])
		
		return expr[len(expr)-1]	
			