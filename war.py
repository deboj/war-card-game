from deck import deck
from card import card
import random
import sys



def war(n=1, verbose=False) :
    x = deck(n)
    y = deck(n)
    x.shuffle()
    y.shuffle()
    while len(x) and len(y) :
        assert len(x) + len(y) == 104*n
        if verbose :
            print ("x:" + str(len(x)) + " y:" + str(len(y)) + " | ") ,
        cx = x.top()
        cy = y.top()
        if verbose :
            print (str(cx) + " versus " + str(cy)) , 
        if cx > cy :
            if verbose :
                print "x wins"
            x.add(cx)
            x.add(cy)
        elif cy > cx :
            if verbose :
                print "y wins"
            y.add(cy)
            y.add(cx)
        else :
            #battle
            if verbose :
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
                if verbose :
                    print "\t" + str(vx) + " versus " + str(vy) 
                if vx > vy :
                    random.shuffle(victory_list)
                    if verbose :
                        print "\tx wins: " + str(map(str,victory_list)) + " length: " + str(len(victory_list)) 
                    x.add_all(victory_list)
                    won = True
                elif vy > vx :
                    if verbose :
                        print "\ty wins: " + str(map(str,victory_list)) + " length: " + str(len(victory_list)) 
                    random.shuffle(victory_list)
                    y.add_all(victory_list)
                    won = True
    if len(x) :
        print "x wins!"
    elif len(y) :
        print "y wins!"
    else :
        print "tie??"
        
n = 1
verbose = False
if len(sys.argv) > 1 :
    if sys.argv[1].lower() in ["v","-v","--v"] :
        if len(sys.argv) > 2 :
            n = int(sys.argv[2])
        verbose = True
    else :
        n = int(sys.argv[1])
war(n, verbose)