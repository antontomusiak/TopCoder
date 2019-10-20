public class LevelUp {

	public int toNextLevel(int[] expNeeded, int received) {
		int n = 0;
		for (int i = 0; i < expNeeded.length; i++) {
			if (expNeeded[i] > received) { 
				n = expNeeded[i] - received;
				break; 
				}
		}
		
		return n;
	}
}