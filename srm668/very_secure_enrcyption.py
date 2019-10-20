class VerySecureEncryption:
	def encrypt(self, message, key, K):
		res = ['' for x in message]
		for i in range(K):
			for j in range(len(key)):
				res[key[j]] = message[j]
			message = ''.join(res)	
		
		return message