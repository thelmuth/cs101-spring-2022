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
    
    def card_rank(self):
        """ Return the rank of this card. """
        index = VALUES.index(self.value)
        return index + 2
        


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
#     print(card.card_rank())
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
#     deck = Deck()
#     print(deck)
#     new_card = deck.draw_card()
#     print("New card:", new_card)
#     print(deck)
#     print(len(deck))

    ### Start working on card game War

    deck = Deck()
    player1 = []
    player2 = []
    
    while len(deck) > 0:
        card = deck.draw_card()
        player1.append(card)
        
        card = deck.draw_card()
        player2.append(card)
        
#     print(player1)
#     print(len(player1))

    turn = 0

    ## Play until someone runs out of cards
    while len(player1) > 0 and len(player2) > 0:
        turn += 1
        
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        
        if card1.card_rank() > card2.card_rank():
            player1.append(card1)
            player1.append(card2)
            print("Player 1 won turn", turn, " --- Cards:", card1, card2)
            print("       Cards in player1:", len(player1), " -- cards in player2:", len(player2))
            
        elif card1.card_rank() < card2.card_rank():
            player2.append(card2)
            player2.append(card1)
            print("Player 2 won turn", turn, card1, card2)
            print("       Cards in player1:", len(player1), " -- cards in player2:", len(player2))
            
        else:
            print("It was a tie!", card1, card2)
            
        print()
        
        
    print("Player 1's cards:", len(player1))
    print("Player 2's cards:", len(player2))


if __name__ == "__main__":
    main()
    