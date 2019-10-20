public class Bits {

	public int minBits(int n) {
		String b = Integer.toString(n, 2);
	return b.length();
	}
}