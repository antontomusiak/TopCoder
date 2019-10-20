public class MovingAverages {
	
	public int[] calculate(String[] times, int n) {
		int m = times.length - n + 1;
		int[] t = new int[times.length];
		int[] av = new int[m];
		for (int i = 0; i < times.length; i++) {
			t[i] = Integer.parseInt(times[i].substring(0, 2)) * 3600 + Integer.parseInt(times[i].substring(3, 5)) * 60 + Integer.parseInt(times[i].substring(6, 8));
		}
		for (int j = 0; j < av.length; j++) {
			int tmp = 0;
			for (int k = j; k < j + n; k++) {
				 tmp += t[k];
			}
			av[j] = tmp / n;
		}
	return av;
	}
}