public class Swimmers {
	public int[] getSwimTimes(int[] distances, int[] speed, int current) {
		int n = speed.length;
		int[] times = new int[n];
		for (int i = 0; i < times.length; i++) {
			if (distances[i] == 0) {
				times[i] = 0;
				continue;
			} else if ((speed[i] - current) <= 0) {
				times[i] = -1;
				continue;
			} else {
				float tmp = (float)distances[i] / (speed[i] + current) + (float)distances[i] / (speed[i] - current);
				times[i] = (int)tmp;
			}
		}
	return times;
    }
}