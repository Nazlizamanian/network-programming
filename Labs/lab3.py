#Lab 3 Nazli Zamanian Gustavsson

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
        return f"{values[self._value]} of {suits[self._suit]}"

# Create a card object
card = CardClass(2, 4)

# Access methods and attributes
print(card.get_value())  # Get the value (4)
print(card.get_suit())   # Get the suit (2

#class cardGameClass:

class CardDeck:
    def __init__(self):
        # Initialize a list to represent the deck of cards
        self.cards = []

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
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        
        self.cards = [f"{value} of {suit}" for suit in suits for value in values]

