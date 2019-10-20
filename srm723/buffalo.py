class BuffaloBuffalo:
	def check(self, s):
		a = "buffalo"
		b = " buffalo"
		c = len(s) - len(a)
		d = c / len(b)
		if len(s) < 7: return "Not good"
		if len(s) == 7 and s == b: return "Good"
		if (c % len(b) == 0) and s == (a + b * d): return "Good" 
		else: return "Not good"