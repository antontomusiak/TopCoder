import java.lang.*;

public class Soccer {

	public int maxPoints(int[] wins, int[] ties) {
		int res = 0;
		for (int i = 0; i < wins.length; i++) {
			res = Math.max(res, (wins[i] * 3 + ties[i]));
		}
	return res;
	}
}