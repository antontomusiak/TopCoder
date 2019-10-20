class Workshop:
	def pictureFrames(self, pieces):
		count = 0
		pieces = sorted(list(pieces))
		for i in range(len(pieces)-2):
			for j in range(i+1, len(pieces)-1):
				for k in range(j+1, len(pieces)):
					if pieces[i] + pieces[j] <= pieces[k]: break
					if pieces[j] + pieces[k] <= pieces[i]: break
					if pieces[k] + pieces[i] <= pieces[j]: break
					else: count += 1
		
		return count 