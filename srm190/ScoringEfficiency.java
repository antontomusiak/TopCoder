public class ScoringEfficiency {

	public double getPointsPerShot(String[] gameLog) {
		double pointsPerShot = 0;
		double totalPoints = 0;
		double goalsAttempted = 0;
		for (int i = 0; i < gameLog.length; i++) {
			switch (gameLog[i]) {
				case "Made 3 point field goal": totalPoints += 3;
												continue;
				case "Made 2 point field goal": totalPoints += 2;
												continue;
				case "Made free throw": 		totalPoints += 1;
												goalsAttempted += (1 * 0.5);
												continue;
				case "Missed free throw":		goalsAttempted += (1 * 0.5);
			}
		}
		goalsAttempted = ((double)gameLog.length - goalsAttempted);
		pointsPerShot = totalPoints / goalsAttempted;
	return pointsPerShot;
	}
}  