class LongLiveZhangzj:
	def donate(self, speech, words):
		count = 0
		#for i in range(len(words)):
		#	for j in speech:
		#		if words[i] == j: count += 1
		#
		for i in words:
			count += speech.count(i)
		
		return count