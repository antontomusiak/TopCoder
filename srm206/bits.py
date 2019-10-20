class Bits:
	def minBits(self, n):
		b = bin(n)[2:]
		if b.endswith('L'): b = b[:len(b)-1]
		return len(b)