class FormatAmt:
	def amount(self, dollars, cents):
		c = '00' + str(cents)
		dollars = str(dollars)
		dolls = [str(dollars[i]) for i in range(len(dollars))]		
		for i in range(len(dolls)-3, -1, -3):
			dolls.insert(i, ',')
		if dolls[0] == ',': dolls.remove(dolls[0])
		
		return '$' + ''.join(dolls) + '.' + c[len(c)-2:len(c)]