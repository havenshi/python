# Example

class Card:
	suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
	ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
			 "8", "9", "10", "Jack", "Queen", "King"]      # narf is used for less confusing to encode 2 as 2, 3 as 3, and so on

	def __init__(self, suit=0, rank=0):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return (self.ranks[self.rank] + " of " + self.suits[self.suit])
		# self.rank as index of into the class attribute named ranks
		
	
	def __cmp__(self, other):                              # compare cards
		# check the suits
		if self.suit > other.suit: return 1
		if self.suit < other.suit: return -1
		# suits are the same... check ranks
		if self.rank > other.rank: 
			if other.rank==1: return -1
			return 1
		if self.rank < other.rank: 
			if self.rank==1: return 1
			return -1
		# ranks are the same... it's a tie
		return 0
	
	

card1 = Card(1, 11)
print card1             # Jack of Diamonds

print card1.suits       # ["Clubs", "Diamonds", "Hearts", "Spades"]
print card1.ranks       # ['narf', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
						# class attributes like ranks and suits are shared by all Card objects
					   

class Deck:
    def __init__(self):
        self.cards = []                               # Deck class has cards as attribute
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))   # each of 4*13 iteration creates a new instance of Card with the current suit and rank, and appends that card to the cards list
                
    def print_deck(self):
        for card in self.cards:
            print card
    
    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"
        return s
        
    def shuffle(self):                                # shuffle
        import random
        num_cards = len(self.cards)
        for i in range(num_cards):            
            j = random.randrange(i, num_cards)        # a <= x < b
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i] # i swap with randrandge(i, num_cards) that hasn't been shuffled yet
            
    def remove(self, card):                           # remove
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False
    
    def pop(self):                                    # deal cards
        return self.cards.pop()
    
    def is_empty(self):
        return (len(self.cards) == 0)
        
deck = Deck()
print deck
#~ Ace of Clubs
 #~ 2 of Clubs
  #~ 3 of Clubs
   #~ 4 of Clubs
     #~ 5 of Clubs
       #~ 6 of Clubs
        #~ 7 of Clubs
         #~ 8 of Clubs
          #~ 9 of Clubs
           #~ 10 of Clubs
            #~ Jack of Clubs
             #~ Queen of Clubs
              #~ King of Clubs
               #~ Ace of Diamonds
                #~ ......        
