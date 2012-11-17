from card import card
from collections import deque
import random # shuffle

class deck :
    def __init__ (self, n=1) :
        """
        the constructor for deck
        adds all 52 cards to its cards array
        n decks
        """
        self.cards = deque()
        #supports multiple decks
        for d in xrange(n) :
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
        try :
            return self.cards.popleft()
        except IndexError :
            return None
    
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

    def add (self, c) :
        """
        a method for adding cards to the bottom of the desk
        """
        self.cards.append(c)
    
    def add_all (self, c) :
        """
        a method for adding multiple cards
        """
        for i in c :
            self.cards.append(i)
    
    def create_stakes (self) :
        """
        a method to create the stakes for a battle.
        always leaves one card for the end.
        if deck is empty, returns None
        """
        if len(self.cards) == 0 :
            return None
        else :
            return [self.top() for i in xrange(min(3,len(self.cards)-1))]
        
    


if (__name__ == "__main__") :
    x = deck()
    x.print_deck()
    print "shuffling..."
    x.shuffle()
    x.print_deck()
    print len(x)
    print x.top()
    print len(x)