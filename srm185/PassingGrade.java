import java.lang.*;

public class PassingGrade {

	public int pointsNeeded(int[] pointsEarned, int[] pointsPossible, int finalExam) {
		int earned = 0;
		float total = finalExam;
		int res = -1;
		for (int i = 0; i < pointsEarned.length; i++) {
			earned += pointsEarned[i];
			total += pointsPossible[i];
		}
		float minPoints = total / 100 * 65;
		minPoints = (int)Math.ceil(minPoints);
		if (earned >= minPoints) {
			res = 0;
		} else if (minPoints - earned > finalExam) {
			res = -1;
		} else {
			res = (int)minPoints - earned;
		}
	return res;
	}
}