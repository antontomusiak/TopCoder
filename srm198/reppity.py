class Reppity:
	def longestRep(self, input):
		res = 0
		if len(input) == 2 and input[0] == input[1]: return 1
		for i in range(len(input)):
			for j in range(i+1, len(input)):
				tmp = input[i:j]
				if input[j:].find(tmp) != -1: res = max(res, len(tmp))
		return res