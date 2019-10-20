public class LetterStrings {

	public int sum(String[] s) {
		int res = 0;
		char d = '-';
		for (int i = 0; i < s.length; i++) {
			for (int j = 0; j < s[i].length(); j++) { 
				if (s[i].charAt(j) != d) {
					res++;
				}
			}
		}
	return res;
	}
}