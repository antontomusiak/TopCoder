import java.lang.*;

public class StairClimb {
	
	public int stridesTaken(int[] flights, int stairsPerStride) {
		float strides = (flights.length - 1) * 2;
		for (int i = 0; i < flights.length; i++) {
			float tmp = flights[i];
			strides += Math.ceil(tmp / stairsPerStride);
			}		
		return (int)strides;
	}
}