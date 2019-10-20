class Justifier:
	def justify(self, textIn):
		textIn = list(textIn)
		n = 0
		for i in range(len(textIn)):
			n = max(n, len(textIn[i]))
		
		for i in range(len(textIn)):
			textIn[i] = ' ' * (n - len(textIn[i])) + textIn[i]
		
		return textIn