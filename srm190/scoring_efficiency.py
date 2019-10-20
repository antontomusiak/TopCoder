class ScoringEfficiency:
	def getPointsPerShot(self, gameLog):
		total_points = gameLog.count("Made 3 point field goal") * 3 + gameLog.count("Made 2 point field goal") * 2 + gameLog.count("Made free throw")
		goals_attempted = len(gameLog) - gameLog.count("Made free throw") * 0.5 - gameLog.count("Missed free throw") * 0.5
		return total_points / goals_attempted  