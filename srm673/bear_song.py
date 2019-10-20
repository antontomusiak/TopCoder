class BearSong:
	def countRareNotes(self, notes):
		rare_notes = 0
		for note in notes:
			if notes.count(note) == 1: rare_notes += 1
		
		return rare_notes