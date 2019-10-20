public class NoOrderOfOperations {

	public int op(int a, char b, char c) {
		int res1 = 0;
		int y = c - '0';
		switch (b) {
			case '-':	res1 = a - y;
						break;
			case '+':	res1 = a + y;
						break;
			case '*':	res1 = a * y;
						break;
			case '/':	res1 = a / y;
						break;
		}
		return res1;
	}
	
	public int evaluate(String expr) {
		int res = 0;
		if (expr.length() == 1) {
			res = Integer.parseInt(expr);
		} else {
			res = expr.charAt(0) - '0';
			for (int i = 2; i < expr.length(); i += 2) {
				int tmp = op(res, expr.charAt(i-1), expr.charAt(i));
				res = tmp;
			}
		}
	return res;
	}
}