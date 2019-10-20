public class Initials
{
	public String getInitials(String name)
	{
		String initials = "" + name.charAt(0);
		char ss = ' ';
		
		for (int i = 1; i < name.length(); i++)
		{
			if (name.charAt(i) == ss)
			{
				initials += name.charAt(i+1);
			}
		}
		return initials;
	}
}