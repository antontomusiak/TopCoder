class CardCount:
	def dealHands(self, numPlayers, deck):
		cards = ['' for i in range(numPlayers)]
		n = len(deck) - len(deck) % numPlayers
		new_deck = deck[:n]
		for i in range(len(new_deck)):
			cards[i%numPlayers] += new_deck[i]
		
		return cards