class Hexspeak:
	def decode(self, ciphertext):
		letters = 'ABCDEF10'
		s = hex(ciphertext)[2:].upper()
		if s.endswith('L'): s = s[:len(s)-1]
		for ch in s:
			if ch not in letters: return 'Error!'
		
		s1 = s.replace("0", "O")
		s2 = s1.replace("1", "I")
		
		return s2