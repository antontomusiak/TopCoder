import java.lang.*;

public class DinkyFish {

	public int monthsUntilCrowded(int tankVolume, int maleNum, int femaleNum) {
		int maxPopulation = tankVolume * 2;
		int currentPopulation = maleNum + femaleNum;
		int months = 0;
		while (currentPopulation <= maxPopulation) {
			int tmp = Math.min(maleNum, femaleNum);
			maleNum += tmp;
			femaleNum += tmp;
			currentPopulation = (maleNum + femaleNum);
			months += 1;
		}
				
		return months;
	}
}