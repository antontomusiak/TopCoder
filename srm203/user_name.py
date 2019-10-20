class UserName:
	def newMember(self, existingNames, newName):
		exists = True
		tmp = 1
		tmp2 = newName
		while exists:
			if tmp2 in existingNames:
				tmp2 = newName + str(tmp)
				tmp += 1
			else: return tmp2