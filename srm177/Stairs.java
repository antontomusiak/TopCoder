public class Stairs {
	
	public int designs(int maxHeight, int minWidth, int totalHeight, int totalWidth) {
		int design = 0;
		for (int i = maxHeight; i > 0; i--) {
			if (totalHeight % i == 0 && totalHeight != i) {
				if ((totalWidth % (totalHeight / i - 1) == 0) && (totalWidth / (totalHeight / i - 1)) >= minWidth) {
					design += 1;
				}
			}
		}			
		return design;
	}
}