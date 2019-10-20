import java.lang.*;

public class RPG {

	public int[] dieRolls(String[] dice) {
		int[] mma = new int[3];
		for (int i = 0; i < dice.length; i++) {
			int tmp1 = Integer.parseInt(dice[i].substring(0, dice[i].indexOf('d')));
			int tmp2 = Integer.parseInt(dice[i].substring((dice[i].indexOf('d')+1), dice[i].length()));			
			mma[0] += tmp1;
			mma[1] += (tmp1 * tmp2);
		}
		double n = (mma[0] + mma[1]) / 2;
		mma[2] = (int)n;
		return mma;
	}
}