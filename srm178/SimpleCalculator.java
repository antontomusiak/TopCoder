import java.lang.*;

public class SimpleCalculator {

	public int calculate(String input) {
		String ops = "-+/*";
		String[] nums = new String[2];
		char op = ' ';
		String num = "";
		int res = 0;
		for (int i = 0; i < input.length(); i++) {
			if (input.charAt(i) == '-' || input.charAt(i) == '+' || input.charAt(i) == '*' || input.charAt(i) == '/') {
				op = input.charAt(i);
				nums[0] = num;
				num = "";
			} else { num += input.charAt(i); }
		}
		nums[1] = num;
		
		switch (op) {
			case '-': res = Integer.parseInt(nums[0]) - Integer.parseInt(nums[1]);
					  break;
					   
			case '+': res = Integer.parseInt(nums[0]) + Integer.parseInt(nums[1]);
					  break;
			
			case '*': res = Integer.parseInt(nums[0]) * Integer.parseInt(nums[1]);
					  break;
			
			case '/': res = Integer.parseInt(nums[0]) / Integer.parseInt(nums[1]);
					  break;
		}
		return res;
	}
}