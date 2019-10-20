class Plusonegame:
	def getorder(self, s):
		counter, plus, res = 0, "+", ""
		new_s = ''.join(sorted(list(s)))
		pluses = new_s.count(plus)
		for i in range(pluses, len(new_s)):
			if counter < int(new_s[i]):
				if pluses >= (int(new_s[i]) - counter):
					res += plus *(int(new_s[i])- counter) + new_s[i]
					pluses = max(0, (pluses - (int(new_s[i])- counter)))
					counter = int(new_s[i])
				else: 
					res += plus * pluses + new_s[i]
					pluses = 0
			else: res += new_s[i]
		
		res += plus * (len(s) - len(res))
		
		return res