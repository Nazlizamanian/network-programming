#Lab3 Nazli Zamanian Gustavsson
import random

class CardClass:
    def __init__(self, suit, value):
        assert 1 <= suit <= 4 and 1 <= value <= 13
        self._suit = suit
        self._value = value

    def get_value(self):
        return self._value

    def get_suit(self):
        return self._suit

    def __str__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        return f"{values[self._value]} of {suits[self._suit - 1]}"

class CardDeck:
    def __init__(self):
        # List to represent the deck of cards.
        self.cards = []
        self.reset()

    def shuffle(self):
        random.shuffle(self.cards)

    def getCard(self):
        # Get and remove a card from the top of the deck
        if self.cards:
            return self.cards.pop()
        else:
            return "No cards left in the deck."

    def size(self):
        # Return the number of cards left in the deck
        return len(self.cards)

    def reset(self):
        # Reset the deck to its initial state
        self.cards = [CardClass(suit, value) for suit in range(1, 5) for value in range(1, 14)]

class CardGame:
    def __init(self):
        self.deck = CardDeck()

    def play_game(self):
        self.deck.shuffle()
        while self.deck.size() > 0:
            card = self.deck.getCard()
            print(f"Card {card} has value {card.get_value()}")

# Create a card object
card = CardClass(2, 4)

# Access methods and attributes
print(card.get_value())  # Get the value (4)
print(card.get_suit())   # Get the suit (2)

# Testing CardDeck
deck = CardDeck()
deck.shuffle()
while deck.size() > 0:
    card = deck.getCard()
    print(f"Card {card} has value {card.get_value()}")
