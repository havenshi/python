# Example1: linked queue
class Queue:                          # linear time
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return (self.length == 0)

    def insert(self, cargo):
        node = Node(cargo)
        node.next = None
        if self.head == None:
            # if list is empty the new node goes first
            self.head = node
        else:
            # find the last node in the list
            last = self.head
            while last.next: 
				last = last.next
            # append the new node
            last.next = node
        self.length = self.length + 1

    def remove(self):                 # FIFO. remove and return an item(the first one that was added) from the queue
        cargo = self.head.cargo 
        self.head = self.head.next
        self.length = self.length - 1
        return cargo


# Example2: improved linked queue
class ImprovedQueue:                 # constant time
    def __init__(self):
        self.length = 0
        self.head   = None
        self.last   = None

    def is_empty(self):
        return (self.length == 0)
        
    def insert(self, cargo):
        node = Node(cargo)
        node.next = None
        if self.length == 0:
            # if list is empty, the new node is head and last
            self.head = self.last = node
        else:
            # find the last node
            last = self.last
            # append the new node
            last.next = node
            self.last = node
        self.length = self.length + 1
        
    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length = self.length - 1
        if self.length == 0:
            self.last = None
        return cargo
        
        
# Example3: priority queue
class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def insert(self, item):
        self.items.append(item)
        
    def remove(self):                   # remove and return the one with the highest priority from the queue
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]: 
				maxi = i
        item = self.items[maxi]     
        self.items[maxi:maxi+1] = []    # remove item
        return item
        
q = PriorityQueue()
q.insert(11)
q.insert(12)
q.insert(14)
q.insert(13)
while not q.is_empty(): print q.remove()
#~ 14
#~ 13
#~ 12
#~ 11


# Example4: the golfer class
class Golfer:
    def __init__(self, name, score):
        self.name = name
        self.score= score

    def __str__(self):
        return "%-16s: %d" % (self.name, self.score)

    def __cmp__(self, other):
        if self.score < other.score: return  1   # less is more
        if self.score > other.score: return -1
        return 0
        
tiger = Golfer("Tiger Woods",    61)
phil  = Golfer("Phil Mickelson", 72)
hal   = Golfer("Hal Sutton",     69)

pq = PriorityQueue()
pq.insert(tiger)
pq.insert(phil)
pq.insert(hal)
while not pq.is_empty(): print pq.remove()
#~ Tiger Woods    : 61
#~ Hal Sutton     : 69
#~ Phil Mickelson : 72


# exercise
class listQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        if self.is_empty():
            return None
        return self.items.pop()
        
class listPriorityQueue:
    def __init__(self): 
        self.length = 0  
        self.head = None 

    def is_empty(self):
        return (self.length == 0)

    def insert(self, cargo):   # linear time
        node = Node(cargo)     
        if self.head == None: 
            self.head = node 
        else:
            if cargo > self.head.cargo:  # if node larger than head, insert node ahead of head 
                node.next = self.head
                self.head = node
            else:                        # insert node ahead of first smaller item
                smaller = self.head          
                while smaller.cargo >= cargo: 
                    previous = smaller       
                    smaller = smaller.next   
                    if smaller == None:      
                        break                
                previous.next = node     # node is larger than smaller, insert node between previous and smaller
                node.next = smaller      # order: previous, previous.next(node), node.next(smaller)
        self.length += 1

    def remove(self):          # constant time
        if self.is_empty():
            return None
        cargo = self.head.cargo
        self.head = self.head.next
        self.length = self.length - 1
        return cargo
