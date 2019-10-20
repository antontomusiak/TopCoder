public class UpDownHiking
{
	public int maxHeight(int N, int A, int B)
	{
		for (int i = 1; i < N; i++){
			if (N == 2)
			{
				return Math.min(A,B);
			}
			if ((A * i) > (B * (N - i)))
			{
				return Math.max((A * (i - 1)), (B * (N - i)));
			}
		}
		
		return A * (N - 1); 
	}
}