public class Average {

	public int belowAvg(int[] math, int[] verbal) {
		int res = 0;
		int sum = 0;
		for (int i = 0; i < math.length; i++) {
			sum += (math[i] + verbal[i]);
		}
		float average = sum / (float)math.length;
		for (int j = 0; j < math.length; j++) {
			if (math[j] + verbal[j] < average) {
				res += 1;
			}
		}
	return res;
	}
}