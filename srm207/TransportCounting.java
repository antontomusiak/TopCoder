public class TransportCounting {

	public int countBuses(int speed, int[] positions, int[] velocities, int time) {
		int res = 0;
		int d = speed * time;
		for (int i = 0; i < positions.length; i++) {
			if (positions[i] == 0 || (positions[i] + velocities[i] * time) <= d) {
				res += 1;
			}
		}
	return res;
	}
}