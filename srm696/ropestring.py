class Ropestring:
	def makerope(self, s):
		dash, dot = '-', '.'
		if dash not in s: return s
		if dot not in s: return s
		ss = s + dot
		even, odd= [], []
		tmp = ''
				
		for i in range(len(ss)):
			if ss[i] == dash: tmp += ss[i]
			if ss[i] == dot and len(tmp) % 2 == 0 and len(tmp) != 0: 
				even.append(tmp + dot)
				tmp = ''
			if ss[i] == dot and len(tmp) % 2 == 1 and len(tmp) != 0: 
				odd.append(tmp + dot)
				tmp = ''
		
		even.sort()
		odd.sort()
		new_s = ''.join(even) + ''.join(odd)
		
		if len(s) > len(new_s):
			return new_s + dot * (len(s) - len(new_s))
		elif len(s) < len(new_s):
			return new_s[:len(new_s)-1]
		else: return new_s