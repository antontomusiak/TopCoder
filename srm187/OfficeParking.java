import java.lang.*;

public class OfficeParking {
	
	public int spacesUsed(String[] events) {
		char space = ' ';
		String arrives = "arrives";
		int count = 0;
		int tmp = 0;
		for (int i = 0; i < events.length; i++) {
			int tmp2 = events[i].indexOf(space) + 1;
			if (events[i].substring(tmp2).equals(arrives)) {
				tmp += 1;
				count = Math.max(count, tmp);
				} else { tmp -= 1;
			}
		}
	return count;
	}
}