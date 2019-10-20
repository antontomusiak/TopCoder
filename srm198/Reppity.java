import java.lang.*;

public class Reppity {

	public int longestRep(String input) {
		int res = 0;
		for (int i = 0; i < input.length(); i++) {
			for (int j = i + 1; j < input.length(); j++) {
				String tmp = input.substring(i, j);
				String tmp2 = input.substring(j);
				if (tmp2.indexOf(tmp) != -1) {
					res = Math.max(res, tmp.length());
				}
			}
		}
	return res;
	}
}