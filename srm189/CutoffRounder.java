import java.lang.*;

public class CutoffRounder {

	public int round(String num, String cutoff) {
		int res = 0;
		float numFloat = Float.parseFloat(num);
		float cutoffFloat = Float.parseFloat(cutoff);
		if (numFloat % 1 > cutoffFloat) {
			res = (int)numFloat + 1;
		} else {
			res = (int)numFloat;
		}
	return res;
	}
}