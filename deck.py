from card import card
import random # shuffle

class deck :
    def __init__ (self) :
        """
        the constructor for deck
        adds all 52 cards to its cards array
        """
        self.cards = []
        for i in xrange(4) :
            for j in xrange(2, 15) :
                self.cards.append(card(j, i))
    
    def print_deck (self) :
        """
        a method that prints the entire deck
        """
        for x in self.cards :
            print x
            
    def top (self) :
        """
        a method for dealing the top card off the deck
        
        return the top card in the deck
        """
        return self.cards.pop()
    
    def shuffle (self) :
        """
        a method for shuffling the deck
        """
        random.shuffle(self.cards)
    
    def __len__ (self) :
        """
        return the number of cards still in this deck
        """
        return len(self.cards) 


if (__name__ == "__main__") :
    x = deck()
    x.print_deck()
    print "shuffling..."
    x.shuffle()
    x.print_deck()
    print len(x)
    print x.top()
    print len(x)