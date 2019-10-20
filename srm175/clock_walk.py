class ClockWalk:
	def finalPosition(self, flips):
		fp, h, t = 0, 0, 0
		for i in range(len(flips)):
			if flips[i] == 'h': h += (i + 1)
			else: t += (i + 1)		
		
		if abs(h - t) % 12 == 0: return 12
		return (12 + (h - t)) % 12