import java.lang.*;

public class Medici {

	public int winner(int[] fame, int[] fortune, int[] secrets) {
		int res = 0;
		int max = 0;
		int count = 0;
		int n = fame.length;
		int[] scores = new int[n];
		for (int i = 0; i < fame.length; i++) {
			int tmp = Math.min(fame[i], fortune[i]);
			scores[i] = Math.min(tmp, secrets[i]);
		}
		for (int j = 0; j < scores.length; j++) {
			if (max < scores[j]) {
				max = scores[j];
				res = j;
			}
		}
		for (int k = 0; k < scores.length; k++) {
			if (max == scores[k]) {
				count++;
			}
		}
		if (count > 1) {
			res = -1;
		}
	return res;
	}
}