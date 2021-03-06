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
    

    def deal(self, hands, num_cards=999):  # a list (or tuple) of hands and the total number of cards
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty(): break   # break if out of cards
            card = self.pop()           # take the top card(removes and returns the last card in the list)
            hand = hands[i % num_hands] # whose turn is next?(nCard % nHand)
            hand.add(card)              # add the card to the hand

deck = Deck()
  
