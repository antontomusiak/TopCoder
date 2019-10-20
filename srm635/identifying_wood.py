class IdentifyingWood:
	def check(self, s, t):
		if s == t: return "Yep, it's wood."
		res = []
		si = 0
		for i in range(len(s)):
			if si == len(t): break
			if s[i] == t[si]:
				res.append(s[i])
				si += 1
		
		if ''.join(res) == t: return "Yep, it's wood."
		return "Nope."