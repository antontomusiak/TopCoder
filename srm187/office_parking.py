class OfficeParking:
	def spacesUsed(self, events):
		sp = ' '
		count = 0
		tmp = 0
		for i in range(len(events)):
			tmp2 = events[i].index(sp) + 1
			if events[i][tmp2:] == 'arrives':
				tmp += 1
				count = max(count, tmp)
			else:
				tmp -= 1
					
		return count