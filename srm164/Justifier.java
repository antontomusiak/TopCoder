import java.lang.*;

public class Justifier {

	public String[] justify(String[] textIn) {
		int n = 0;
		String sp = " ";
		for (int i = 0; i < textIn.length; i++) {
			n = Math.max(n, textIn[i].length());
		}
		for (int i = 0; i < textIn.length; i++) {
			int d = n - textIn[i].length();
			textIn[i] = repeat(" ", d) + textIn[i];
		}
		
		return textIn;
	}
	
	public String repeat(String str, int n) {
		StringBuilder sb = new StringBuilder(n);
		for (int i = 0; i < n; i++) {
			sb.append(str);
			}
		return sb.toString();
	}
}