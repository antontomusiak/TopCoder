import math

class PalindromePrime:
	def count(self, L, R):
		def isPrime(n):
			if n == 1: return False
			if n == 2: return True
			m = int(math.sqrt(n))
			for i in range(2, m+1):
				if n % i == 0: return False
			return True
		
		def isPalindrome(n1):
			n = str(n1)
			m = int(len(n) / 2)
			if len(n) == 1: return True
			for i in range(m):
				j = len(n) - 1 - i
				if n[i] != n[j]: return False
			return True
			
		
		pp = 0
		for i in range(L, R+1):
			if  (isPrime(i) and isPalindrome(i)): pp += 1
		
		return pp