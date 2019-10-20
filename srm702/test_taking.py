class TestTaking:
	def findMax(self, questions, guessed, actual):
		t_count = min(guessed, actual)
		f_count = min(questions - guessed, questions - actual)
		return t_count + f_count