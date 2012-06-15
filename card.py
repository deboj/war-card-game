class card :
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__ (self) :
        result = ""
        if (self.rank < 11) :
            result += str(self.rank)
        else :
            face_cards = ['J', 'Q', 'K', 'A']
            result += face_cards[self.rank - 11]
        result += " of "
        suits = ['Clubs', 'Diamonds', 'Spades', 'Hearts']
        result += suits[self.suit]
        return result