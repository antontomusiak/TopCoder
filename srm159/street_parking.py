class StreetParking:
	def freeParks(self, street):
		st = '--' + street + '-'
		s = [0 for x in st]
		for i in range(2, len(st)):
			if st[i] == 'S':
				s[i-1], s[i], s[i+1] = 1, 1, 1
			if st[i] == 'B':
				s[i-2], s[i-1], s[i] = 1, 1, 1
			if st[i] == 'D':
				s[i] = 1
		s = s[2:len(s)-1]
		return s.count(0)