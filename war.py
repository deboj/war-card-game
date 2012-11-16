from deck import deck
from card import card
import random

x = deck()
y = deck()
x.shuffle()
y.shuffle()

while len(x) and len(y) :
    assert len(x) + len(y) == 104
    cx = x.top()
    cy = y.top()
    print (str(cx) + " versus " + str(cy)) ,
    if cx > cy :
        print "x wins"
        x.add(cx)
        x.add(cy)
    elif cy > cx :
        print "y wins"
        y.add(cy)
        y.add(cx)
    else :
        #battle
        print "battle!"
        won = False
        victory_list = [cx, cy]
        while not won :
            stake_x = x.create_stakes()
            if stake_x is None :
                break
            stake_y = y.create_stakes()
            if stake_y is None :
                break
            vx = x.top()
            vy = y.top()
            victory_list += (stake_x + stake_y + [vx, vy])
            print "\t" + str(vx) + " versus " + str(vy)
            if vx > vy :
                random.shuffle(victory_list)
                print "\tx wins: " + str(map(str,victory_list)) + " length: " + str(len(victory_list))
                x.add_all(victory_list)
                won = True
            elif vy > vx :
                random.shuffle(victory_list)
                print "\ty wins: " + str(map(str,victory_list)) + " length: " + str(len(victory_list))
                y.add_all(victory_list)
                won = True



if len(x) :
    print "x wins!"
elif len(y) :
    print "y wins!"
else :
    print "tie??"