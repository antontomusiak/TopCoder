public class CardCount {
	public String[] dealHands(int numPlayers, String deck) {
		String[] hands = new String[numPlayers];
		int n = deck.length() - deck.length() % numPlayers;
		String newDeck = deck.substring(0, n);
		for (int i = 0; i < hands.length; i++) {
			hands[i] = "";
			}
		for (int i = 0; i < newDeck.length(); i++) {
			hands[i % numPlayers] += newDeck.charAt(i);
			}
		return hands;
		}
	} 