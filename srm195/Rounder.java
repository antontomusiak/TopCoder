public class Rounder {

	public int round(int n, int b) {
		int res = 0;
		if (n % b == 0) {
			res = n;
		} else if (((float)n / (float)b - n / b) < 0.5) {
			res = (n / b) * b;
		} else { res =  ((n / b) + 1) * b;
		}
	return res;
	}
}