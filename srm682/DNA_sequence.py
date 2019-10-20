class DNASequence:
	def longestDNASequence(self, sequence):
		s = sequence + ' '
		dna = 'ACGT'
		l = 0
		for i in range(len(s)-1):
			tmp = 0
			if s[i] in dna:
				tmp = 1
				for j in range(i+1, len(s)):
					if s[j] in dna: tmp += 1
					else: 
						l = max(l, tmp)
						break
		return l