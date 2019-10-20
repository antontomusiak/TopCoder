class ElectronicPetEasy:
	def isDifficult(self, st1, p1, t1, st2, p2, t2):
		pet1 = [(st1 + i*p1) for i in range(t1)]
		pet2 = [(st2 + i*p2) for i in range(t2)]
		for f in pet1:
			if f in pet2: return 'Difficult'
		
		return 'Easy'