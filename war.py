from deck import deck
from card import card

x = deck()
y = deck()

while len(x) and len(y) :
    x.top()
    #y.top()

if len(x) :
    print "x wins!"
elif len(y) :
    print "y wins!"