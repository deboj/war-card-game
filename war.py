from deck import deck
from card import card
import random
import sys
import time



def war(n=1, verbose=False, stagger=False) :
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
                print "\nBATTLE!" 
            if stagger :
                time.sleep(1.3)
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
                if stagger :
                    time.sleep(.65)
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
            if stagger :
                time.sleep(.65)
        if stagger :
            time.sleep(.65)
    if len(x) :
        print "x wins!"
    elif len(y) :
        print "y wins!"
    else :
        print "tie??"
        

verbose = False
stagger = False

if "-v" in sys.argv :
    verbose = True
if "-s" in sys.argv :
    stagger = True

try :
    n = int(sys.argv[[verbose,stagger].count(True)+1])
except :
    n = 1

war(n, verbose, stagger)