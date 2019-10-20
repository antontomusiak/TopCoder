import java.lang.*;

public class StringMult {

	public String times(String sFactor, int iFactor) {
		String res = "";
		if (iFactor > 0) {
			res = new String(new char[iFactor]).replace("\0", sFactor);
		} else if (iFactor < 0) {
			String reverse = new StringBuffer(sFactor).reverse().toString();
			res = new String(new char[Math.abs(iFactor)]).replace("\0", reverse);
		}	
	return res;
	}
}