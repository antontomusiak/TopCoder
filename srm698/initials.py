class Initials:
	def getInitials(self, name):
		initials = name[0]
		ws = " "
		for i in range(1,len(name)):			
			if name[i] == ws: initials += name[i+1]
		
		return initials