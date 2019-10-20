class Robofactory:
	def reveal(self, query, answer):
		#if len(query) == 1: return 0
		#if query[0] % 2 == 1 and query[1] % 2 == 1: return 0
		all_odd = True
		for i in range(1, len(query)):
			if query[i-1] % 2 == 1:
				if query[i] % 2 == 1 and answer[i] == "Even": return i
				if query[i] % 2 == 0 and answer[i] == "Odd": return i
			else: all_odd = False
		if all_odd: return 0
		return -1