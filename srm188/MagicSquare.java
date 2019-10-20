import java.lang.*;

public class MagicSquare {

	public int missing(int[] square) {
		int mn = 0;
		int ind = 0;
		for (int i = 0; i < square.length; i++) {
			if (square[i] == -1) {
				ind = i;
			}
		}
		if (ind < 3) {
			mn = square[3] + square[4] + square[5] - square[0] - square[2] - square[1] - 1;
			} else if (ind >= 3 && ind < 6) {
				mn = square[0] + square[2] + square[1] - 1 - square[3] - square[4] - square[5];
			} else {
				mn = square[0] + square[2] + square[1] - 1 - square[6] - square[7] - square[8];
		}
	return mn;
	}
}