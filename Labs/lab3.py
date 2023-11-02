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
        values = ["One","Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
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

while deck.size() > 0:
    card = deck.getCard()
    if card:
        print(f"Card {card} has value {card.getValue()}")
