war-card-game
=============

The greatest card game, now simulated on the command line.


to simulate a game with no output, just run it with python: 

    $ python war.py [options] [num_decks]


there are two players: x and y. each starts with num_decks of its own full decks of cards (specifying nothing defaults to 1). when the simulation has finished, it will print which player won the game. place your bets now!

    -v option (verbose)
      to see what happens during the simulation, run it with the -v option (verbose).

    -s option (staggered output)
      to see the simulation play out as if it were in real time, run it with the -s option (staggered output). have fun watching!
	
ex. output (3 decks):
------------------------------------------------------------------------------------
	x:301 y:11 |  9 of Hearts versus 8 of Spades x wins
	x:302 y:10 |  8 of Hearts versus J of Hearts y wins
	x:301 y:11 |  4 of Clubs versus 7 of Diamonds y wins
	x:300 y:12 |  8 of Spades versus K of Hearts y wins
	x:299 y:13 |  4 of Diamonds versus Q of Hearts y wins
	x:298 y:14 |  6 of Spades versus 9 of Hearts y wins
	x:297 y:15 |  3 of Spades versus 2 of Hearts x wins
	x:298 y:14 |  A of Spades versus A of Clubs 
	BATTLE!
		A of Diamonds versus J of Hearts
		x wins: ['3 of Diamonds', 'J of Diamonds', 'A of Spades', '7 of Clubs', 'A of Diamonds', 'A of Clubs', 'J of Diamonds', '3 of Hearts', 'J of Hearts', '2 of Diamonds'] length: 10
	x:303 y:9 |  Q of Diamonds versus 8 of Hearts x wins
	x:304 y:8 |  10 of Diamonds versus 7 of Diamonds x wins
	x:305 y:7 |  9 of Clubs versus 4 of Clubs x wins
	x:306 y:6 |  A of Hearts versus K of Hearts x wins
	x:307 y:5 |  9 of Clubs versus 8 of Spades x wins
	x:308 y:4 |  7 of Clubs versus Q of Hearts y wins
	x:307 y:5 |  3 of Diamonds versus 4 of Diamonds y wins
	x:306 y:6 |  Q of Clubs versus 9 of Hearts x wins
	x:307 y:5 |  J of Clubs versus 6 of Spades x wins
	x:308 y:4 |  Q of Clubs versus Q of Hearts 
	BATTLE!
		9 of Clubs versus 3 of Diamonds
		x wins: ['10 of Hearts', '8 of Hearts', 'Q of Clubs', '7 of Clubs', 'Q of Hearts', '5 of Diamonds', '4 of Diamonds', '3 of Diamonds', '9 of Clubs'] length: 9
	x wins!
