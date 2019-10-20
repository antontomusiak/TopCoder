class CCipher:
	def decode(self, cipherText, shift):
		abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		res = ''
		for l in cipherText:
			if abc.index(l) - shift < 0: 
				ind = 25 - abs(abc.index(l) - shift + 1)
				res += abc[ind]
			else: 
				ind = abc.index(l) - shift
				res += abc[ind]
		return res