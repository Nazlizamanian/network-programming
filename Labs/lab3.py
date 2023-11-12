#Lab 3 Nazli Zamanian Gustavsson
import random

class Card:
    def __init__(self, suit, value): #Constructor method intializes
        assert 1 <= suit <= 4 and 1 <= value <= 13
        self._suit = suit
        self._value = value

    def getValue(self): #Some getters.
        return self._value

    def getSuit(self):
        return self._suit

    def __str__(self): #returns our string putted together.
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        values = ["One","Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        return f"{values[self._value - 1]} of {suits[self._suit - 1]}"


class CardDeck:
    def __init__(self):
        self._cards = []
        for suit in range(1, 5): 
            for value in range(1, 14):
                self._cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self._cards)

    def getCard(self):
        if not self._cards:
            return None
        return self._cards.pop()

    def size(self):
        return len(self._cards)

    def reset(self): #Reinitalizing the cards. 
        self.__init__()

# Test code
deck = CardDeck()
deck.shuffle()
current_size = deck.size()

while deck.size() > 0:
    card = deck.getCard()
    if card:
        print(f"Card {card} has value {card.getValue()}")
   
def test_card_class():
    card = Card(1, 11)  # Jack of Spades
    assert card.getValue() == 11
    assert card.getSuit() == 1
    assert str(card) == "Jack of Spades"


def test_card_deck_class():
    # Create a CardDeck instance
    deck = CardDeck()
    assert deck.size() == 52

    # Shuffle the deck
    deck.shuffle()

    # Draw and check each card from the shuffled deck
    drawn_cards = []
    while deck.size() > 0:
        card = deck.getCard()
        if card:
            drawn_cards.append(card)

    # Verify that the number of drawn cards matches the size of the initial deck
    assert len(drawn_cards) == 52

    # Verify that all drawn cards are unique
    unique_cards = set(drawn_cards)
    assert len(unique_cards) == 52

    # Reset the deck
    deck.reset()

    assert deck.size() == 52

    print("test_card_deck_class passed")

if __name__ == "__main__":
    test_card_deck_class()
