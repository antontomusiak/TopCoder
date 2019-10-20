public class Education {

	public int minimize(String desire, int[] tests) {
		int res = 0;
		String grades = "ABCD";
		int[] points = {90, 80, 70, 60};
		int totalPoints = points[grades.indexOf(desire)] * (tests.length + 1);
		int earned = 0;
		for (int i: tests) {
			earned += i;
		}
		res = totalPoints - earned;
		if (res <= 0) {
			res = 0;
		} else if (res > 100) {
			res = -1;
		}
	return res;
	}
} 