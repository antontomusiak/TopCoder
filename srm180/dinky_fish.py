class DinkyFish:
	def monthsUntilCrowded(self, tankVolume, maleNum, femaleNum):
		max_population = tankVolume * 2
		current_population = maleNum + femaleNum
		months = 0
		while current_population <= max_population:
			tmp = min(maleNum, femaleNum)
			maleNum += tmp
			femaleNum += tmp
			current_population = (maleNum + femaleNum)
			months += 1
		
		return months