public class AlternatingString
{
	public int maxLength(String s)
	{
		int count = 0;
		int s_l = s.length();
		int tmp = 1;
		for (int i = 0; i < s_l - 1; i++)
		{	if (s_l == 1)
			{ 
				return 1;
			}
			if (s.charAt(i) != s.charAt(i+1))
			{ 
				tmp++;
			} else 
				{
				count = Math.max(tmp, count);
				tmp = 1;
				}
			}
		
		return Math.max(count, tmp);
	}
}