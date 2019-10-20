class ValueOfString:
	def findValue(self, s):
		value = 0
		abc = 'abcdefghijklmnopqrstuvwxyz'
		num_list = [abc.index(s[i])+1 for i in range(len(s))]
		for num in num_list:
			value += num * len([x for x in num_list if x <= num])
		
		return value