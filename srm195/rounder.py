class Rounder:
	def round(self, n, b):
		if n % b == 0: return n
		if (float(n) / float(b) - n / b) < 0.5: return  (n / b) * b
		else: return ((n / b) + 1) * b