public class BettingMoney {

	public int moneyMade(int[] amounts, int[] centsPerDollar, int finalResult) {
		int win = 0;
		int res = 0;
		int total = 0;
		for (int i = 0; i < amounts.length; i++) {
			if (i == finalResult) {
				win = amounts[i] * centsPerDollar[i] + amounts[i] * 100;
				total += amounts[i];
			} else { total += amounts[i];
			}
		}
		res = total * 100 - win;
	
	return res;
	}
}	