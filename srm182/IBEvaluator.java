import java.lang.*;

public class IBEvaluator {

	public int[] getSummary(int[] predictedGrades, int[] actualGrades) {
		int[] diff = new int[7];
		int n = predictedGrades.length;
		for (int i = 0; i < diff.length; i++) {
			diff[i] = 0;
		}
		for (int j = 0; j < n; j++) {	
			int tmp = Math.abs(predictedGrades[j]- actualGrades[j]);
			diff[tmp] += 1;
		}
		for (int l = 0; l < diff.length; l++) {
			float tmp = diff[l] / (float)n;
			diff[l] = (int)Math.floor(tmp * 100);
		}
		
	return diff;
	}
} 