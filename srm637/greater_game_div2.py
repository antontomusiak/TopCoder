class GreaterGameDiv2:
	def calc(self, snuke, sothe):
		snuke_points = 0
		for i in range(len(snuke)):
			if snuke[i] > sothe[i]: snuke_points += 1
		
		return snuke_points