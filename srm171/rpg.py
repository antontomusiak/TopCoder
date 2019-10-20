class RPG:
	def dieRolls(self, dice):
		mma = [0, 0, 0]
		for i in range(len(dice)):
			mma[0] += int(dice[i][:dice[i].index('d')])
			mma[1] += int(dice[i][dice[i].index('d')+1:]) * int(dice[i][:dice[i].index('d')])
		
		mma[2] = (mma[0] + mma[1]) / 2
		
		return mma