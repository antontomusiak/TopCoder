class Time:
	def whatTime(self, seconds):
		h = seconds/3600
		m = (seconds%3600) / 60
		s = seconds - h * 3600 - m * 60
		
		time = str(h)+ ':' + str(m) + ':' + str(s)
		return time  