class PrefixCode:
	def isOne(self, words):
		ind = 51
		pref = False
		for i in range(len(words)-1):
			for j in range(i+1, len(words)):
				pre = min(words[i], words[j])
				word = max(words[i], words[j])
				if word.startswith(pre):
					ind = min(words.index(pre), ind)
					pref = True
		if pref: return 'No, ' + str(ind)		
		return 'Yes'