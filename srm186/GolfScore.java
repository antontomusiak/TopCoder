import java.util.*;

public class GolfScore {
	
	public int tally(int[] parValues, String[] scoreSheet) {
		int res = 0;
		for (int i = 0; i < parValues.length; i++) {
			switch (scoreSheet[i]) {
			
			case "hole in one":  res += 1;
								 continue;
			case "triple bogey": res += (parValues[i] + 3);
								 continue;
			case "double bogey": res += (parValues[i] + 2);
								 continue;
			case "bogey":		 res += (parValues[i] + 1);
								 continue;
			case "par": 		 res += parValues[i];
								 continue;
			case "birdie":		 res += (parValues[i] - 1);
								 continue;
			case "eagle":		 res += (parValues[i] - 2);
								 continue;
			case "albatross":    res += (parValues[i] - 3);
								 continue;
			}
		}
	return res;
	}
}