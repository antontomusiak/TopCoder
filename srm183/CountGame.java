public class CountGame {

	public int howMany(int maxAdd, int goal, int next) {
		int res = -1;
		for (int i = goal; i > next - 1; i -= (maxAdd + 1)) {
			if (i - next + 1 <= maxAdd) {
				 res = (i - next + 1);
			}
		}
	return res;
	}
}