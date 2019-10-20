class ListeningSongs:
	def listen(self, duration1, duration2, minutes, T):
		d1 = sorted(list(duration1))
		d2 = sorted(list(duration2))
		if len(d1) < T or len(d2) < T: return -1
		if (sum(d1[:T]) + sum(d2[:T])) > minutes * 60: return -1		
		t_left = minutes * 60 - (sum(d1[:T]) + sum(d2[:T]))
		d3 = sorted(d1[T:] + d2[T:])
		T = T * 2
		for i in range(len(d3)):
			if d3[i] <= t_left: 
				t_left -= d3[i]
				T += 1
			else: return T
		
		return T