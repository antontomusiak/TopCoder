import java.util.*;

public class ClockWalk {

	public int finalPosition(String flips) {
		int h = 0;
		int t = 0;
		for (int i = 0; i < flips.length(); i++) {
			if (flips.charAt(i) == 'h') { 
				h += (i + 1);
			} else { 
				t += (i + 1);
			}
		}			
		int c = (h - t) % 12;
		c = (c + 12) % 12;
		 
		if (c == 0) {
			c = 12;
		} 
		
		return c;
	}
}