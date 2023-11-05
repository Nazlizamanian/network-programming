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
   
# def test_card_class():
#     card = Card(1, 11)  # Jack of Spades
#     assert card.getValue() == 11
#     assert card.getSuit() == 1
#     assert str(card) == "Jack of Spades"

# # Test the CardDeck class
# def test_card_deck_class():
#     deck = CardDeck()

#     # Test shuffle and size
#     deck.shuffle()
#     assert deck.size() == 52

#     # Test getCard
#     card = deck.getCard()
#     assert card.getValue() == 13  # King
#     assert card.getSuit() == 4  # Clubs

#     # Test reset
#     deck.reset()
#     assert deck.size() == 52

# # Run the test cases
# if __name__ == "__main":
#     test_card_class()
#     test_card_deck_class()
#     print("All test cases passed.")