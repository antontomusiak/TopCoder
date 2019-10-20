class Xylophone:
	def countKeys(self, keys):
		keys_s = set()
		for i in keys:
			if (i % 7 == 0):
				keys_s.add((i % 7) + 7)
			else: keys_s.add((i % 7))
		
		return len(keys_s)