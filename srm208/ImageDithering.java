public class ImageDithering {

	public int count(String dithered, String[] screen) {
		int res = 0;
		for (int i = 0; i < screen.length; i++) {
			for (int j = 0; j < screen[i].length(); j++) {
				char tmp = screen[i].charAt(j);
				if (dithered.indexOf(tmp) != -1) {
					res += 1;
				}
			}
		}
	return res;
	}
}