import java.util.*;

public class CrossWord {

	public int countWords(String[] board, int size) {
		int count = 0;
		char dot = '.';
		for (int i = 0; i < board.length; i++) {
			int tmp = 0;
			for (int j = 0; j < board[i].length(); j++) {
				if (board[i].charAt(j) == dot) {
					tmp += 1;
				} else {
					if (tmp == size) {count++;}
					tmp = 0;
				}			
				
			}
			
			if (tmp == size) {
				count++;
			}
		}
			
		return count;
	}

 }