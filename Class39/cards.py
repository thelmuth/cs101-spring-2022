import random

### These are global constants, and hence all caps
VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]


class PlayingCard:
    """Represents a single playing card from a standard deck."""
    
    def __init__(self, v, s):
        """ This constructs a playing card with value v and suit s. """
        self.value = v
        self.suit = s

    def __str__(self):
        """ Return a string representation of the object."""
        return str(self.value) + " of " +  self.suit

    def __repr__(self):
        """ Return a string representation of the object."""
        return str(self.value) + " of " +  self.suit


class Deck:
    """Represents a deck of cards that can be shuffled and dealt, one at a time."""
    
    def __init__(self):
        """Creates a new deck of 52 cards."""
        
        self.pack = []
        for suit in SUITS:
            for value in VALUES:
                card = PlayingCard(value, suit)
                self.pack.append(card)
        random.shuffle(self.pack)
        
        
    def __str__(self):
        return "DECK:" + str(self.pack)
    
    def draw_card(self):
        """ Removes and returns a card from the deck."""
        
        return self.pack.pop(0)
    
    def __len__(self):
        """Finds and returns the number of cards in this deck."""
        return len(self.pack)
        

def main():
 
#     card = PlayingCard("Q", "Hearts")
#     print(card)
# #     print(card.value)
# #     print(card.suit)
# 
#     seven_diamonds = PlayingCard(7, "Diamonds")
#     print(seven_diamonds)
    
    ### Let's make a deck of 52 cards as a list of PlayingCard objects
#     deck = []
#     for suit in SUITS:
#         for value in VALUES:
#             card = PlayingCard(value, suit)
#             deck.append(card)
#     random.shuffle(deck)
#             
#     print(deck)

    ### Now use our Deck class
    deck = Deck()
    print(deck)
    new_card = deck.draw_card()
    print("New card:", new_card)
    print(deck)
    print(len(deck))



if __name__ == "__main__":
    main()
    