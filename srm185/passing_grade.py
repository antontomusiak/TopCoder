import math

class PassingGrade:
	def pointsNeeded(self, pointsEarned, pointsPossible, finalExam):
		min_points = math.ceil((sum(pointsPossible) + finalExam) / float(100) * 65)
		if sum(pointsEarned) >= min_points: return 0
		if min_points - sum(pointsEarned) > finalExam: return -1
		return min_points - sum(pointsEarned)