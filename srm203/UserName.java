import java.lang.*;

public class UserName {

	public String newMember(String[] existingNames, String newName) {
		boolean exists = true;
		int tmp = 1;
		String tmp2 = newName;
		while (exists) { 
			boolean found = false;
			for (int i = 0; i < existingNames.length; i++) {
				if (existingNames[i].equals(tmp2)) {
					found = true;
					break;
				}
			}
			if (found) {
				tmp2 = newName + Integer.toString(tmp);
				tmp += 1;
			} else {
				exists = false;
			}
		}
	return tmp2;
	}
}  