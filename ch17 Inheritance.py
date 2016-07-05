from ch16 import *

class Hand(Deck):                  # Hand inherits Deck
	def __init__(self, name=""):
	   self.cards = []
	   self.name = name
	   
	def add(self,card):
		self.cards.append(card)

	def __str__(self):             # overrides __str__ method in the Deck class
		s = "Hand " + self.name
		if self.is_empty():
			s = s + " is empty\n"
		else:
			s = s + " contains\n"
		return s + Deck.__str__(self)
		
		
deck = Deck()
deck.shuffle()
hand = Hand("frank")
deck.deal([hand], 5)   # nHand=4
print hand             # each time get different result
#~ Hand frank contains
#~ 2 of Spades
 #~ 3 of Spades
  #~ 4 of Spades
   #~ Ace of Hearts
	#~ 9 of Clubs




class CardGame:
	def __init__(self):
		self.deck = Deck()
		self.deck.shuffle()


class OldMaidHand(Hand):
	def remove_matches(self):   # traverse the copy(original_cards) while removing cards from the original(cards)
		count = 0
		original_cards = self.cards[:]
		for card in original_cards:
			match = Card(3 - card.suit, card.rank) # match card has the same rank and the other suit of the same color
			if match in self.cards:
				self.cards.remove(card)
				self.cards.remove(match)
				print "Hand %s: %s matches %s" % (self.name, card, match)
				count = count + 1
		return count

game = CardGame()
hand = OldMaidHand("frank")
game.deck.deal([hand], 13)
print hand
#~ Hand frank contains
#~ Ace of Spades
 #~ 2 of Diamonds
  #~ 7 of Spades
   #~ 8 of Clubs
	#~ 6 of Hearts
	 #~ 8 of Spades
	  #~ 7 of Clubs
	   #~ Queen of Clubs
		#~ 7 of Diamonds
		 #~ 5 of Clubs
		  #~ Jack of Diamonds
		   #~ 10 of Diamonds
			#~ 10 of Hearts
			
hand.remove_matches()
#~ Hand frank: 7 of Spades matches 7 of Clubs
#~ Hand frank: 8 of Spades matches 8 of Clubs
#~ Hand frank: 10 of Diamonds matches 10 of Hearts

print hand
#~ Hand frank contains
#~ Ace of Spades
 #~ 2 of Diamonds
  #~ 6 of Hearts
   #~ Queen of Clubs
	#~ 7 of Diamonds
	 #~ 5 of Clubs
	  #~ Jack of Diamonds

class OldMaidGame(CardGame):
	def play(self, names):
		# remove Queen of Clubs
		self.deck.remove(Card(0,12))

		# make a hand for each player
		self.hands = []                           # Deck>>deal>>hands
		for name in names:                        # OldMaidGame>>play>>names
			self.hands.append(OldMaidHand(name))

		# deal the cards
		self.deck.deal(self.hands)
		print "---------- Cards have been dealt"
		self.printHands()

		# remove initial matches
		matches = self.removeAllMatches()
		print "---------- Matches discarded, play begins"
		self.printHands()

		# play until all 50 cards are matched
		turn = 0
		numHands = len(self.hands)
		while matches < 25:
			matches = matches + self.playOneTurn(turn)
			turn = (turn + 1) % numHands

		print "---------- Game is Over"
		self.printHands()
		
		
		
		def remove_all_matches(self):
			count = 0
			for hand in self.hands:
				count = count + hand.remove_matches()  # how many matched pairs in total hands
			return count

		def play_one_turn(self, i):                    # indicates whose turn it is
			if self.hands[i].is_empty():               # player is out of the game if his hand is empty
				return 0
			neighbor = self.find_neighbor(i)           
			pickedCard = self.hands[neighbor].popCard()# take one card from neighbor
			self.hands[i].add(pickedCard)
			print "Hand", self.hands[i].name, "picked", pickedCard
			count = self.hands[i].remove_matches()
			self.hands[i].shuffle()
			return count

		def find_neighbor(self, i):  # start with left player and continue around the circle until it finds a player that still has cards
			numHands = len(self.hands)
			for next in range(1,numHands):
				neighbor = (i + next) % numHands
				if not self.hands[neighbor].is_empty():
					return neighbor

		def printHands(self):
			for hand in self.hands:
				print hand



import cards
game = cards.OldMaidGame()
game.play(["Allen","Jeff","Chris"])
#~ ---------- Cards have been dealt
#~ Hand Allen contains
#~ King of Hearts
 #~ Jack of Clubs
  #~ Queen of Spades
   #~ King of Spades
    #~ 10 of Diamonds
#~ 
#~ Hand Jeff contains
#~ Queen of Hearts
 #~ Jack of Spades
  #~ Jack of Hearts
   #~ King of Diamonds
    #~ Queen of Diamonds
#~ 
#~ Hand Chris contains
#~ Jack of Diamonds
 #~ King of Clubs
  #~ 10 of Spades
   #~ 10 of Hearts
    #~ 10 of Clubs
#~ 
#~ Hand Jeff: Queen of Hearts matches Queen of Diamonds
#~ Hand Chris: 10 of Spades matches 10 of Clubs
#~ ---------- Matches discarded, play begins
#~ Hand Allen contains
#~ King of Hearts
 #~ Jack of Clubs
  #~ Queen of Spades
   #~ King of Spades
    #~ 10 of Diamonds
#~ 
#~ Hand Jeff contains
#~ Jack of Spades
 #~ Jack of Hearts
  #~ King of Diamonds
#~ 
#~ Hand Chris contains
#~ Jack of Diamonds
 #~ King of Clubs
  #~ 10 of Hearts
#~ 
#~ Hand Allen picked King of Diamonds
#~ Hand Allen: King of Hearts matches King of Diamonds
#~ Hand Jeff picked 10 of Hearts
#~ Hand Chris picked Jack of Clubs
#~ Hand Allen picked Jack of Hearts
#~ Hand Jeff picked Jack of Diamonds
#~ Hand Chris picked Queen of Spades
#~ Hand Allen picked Jack of Diamonds
#~ Hand Allen: Jack of Hearts matches Jack of Diamonds
#~ Hand Jeff picked King of Clubs
#~ Hand Chris picked King of Spades
#~ Hand Allen picked 10 of Hearts
#~ Hand Allen: 10 of Diamonds matches 10 of Hearts
#~ Hand Jeff picked Queen of Spades
#~ Hand Chris picked Jack of Spades
#~ Hand Chris: Jack of Clubs matches Jack of Spades
#~ Hand Jeff picked King of Spades
#~ Hand Jeff: King of Clubs matches King of Spades
#~ ---------- Game is Over
#~ Hand Allen is empty
#~ 
#~ Hand Jeff contains
#~ Queen of Spades
#~ 
#~ Hand Chris is empty
