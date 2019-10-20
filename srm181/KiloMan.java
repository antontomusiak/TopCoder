public class KiloMan {

	public int hitsTaken(int[] pattern, String jumps) {
		int res = 0;
		for (int i = 0; i < pattern.length; i++) {
			if ((pattern[i] <= 2 && jumps.charAt(i) == 'S') || (pattern[i] > 2 && jumps.charAt(i) == 'J')) {
			 	res += 1;
			 }
		}		
		return res;
	}
}