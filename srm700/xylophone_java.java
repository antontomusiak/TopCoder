import java.util.*;

public class Xylophone
{
	public int countKeys(int[] keys)
	{
		Set<Integer> keysSet = new HashSet<Integer>();
		
		for(int i: keys){			
			if (i % 7 == 0){
				keysSet.add(7);
			}
		    else{
				keysSet.add(i % 7);
		    }
		}
		
	return keysSet.size();
	}
}