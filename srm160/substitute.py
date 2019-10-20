class Substitute:
	def getValue(self, key, code):
		res = ''
		for l in code:
			if l in key and  key.index(l) == len(key) - 1: res += '0'
			if l in key and  key.index(l) != len(key) - 1: res += str(key.index(l)+1)
		
		return int(res)