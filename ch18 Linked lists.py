# Example1: Node class
class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)

node = Node("test")
print node                               # test

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3



def print_list(node):
    while node:
        print node,
        node = node.next
    print

print_list(node1)                        # 1 2 3



def print_backward(list):
    if list == None: return
    head = list
    tail = list.next
    print_backward(tail)
    print head,
    
print_backward(node1)                    # 3 2 1

print

def removeSecond(list):
    if list == None: return
    first = list
    second = list.next
    # make the first node refer to the third
    first.next = second.next
    # separate the second node from the rest of the list
    second.next = None
    return second
    
#~ print_list(node1)                       # 1 2 3
#~ removed = removeSecond(node1)
#~ print_list(removed)                     # 2
#~ print_list(node1)                       # 1 3



def print_backward_nicely(list) :          # a wrapper
    print "[",
    if list != None :
        head = list
        tail = list.next
        print_backward(tail)               # a helper
        print head,
    print "]",

print_backward_nicely(node1)               # [ 3 2 1 ]

print


# Example2: LinkedList class
class LinkedList:                          # a wrapper
    def __init__(self):
        self.length = 0
        self.head   = None
    def print_backward(self):
        print "[",
        if self.head != None:
            self.head.print_backward()     # invoking the helper because self.head is a Node object
        print "]",

    def addFirst(self, cargo):             # takes an item of cargo as an argument and puts it at the beginning of the list
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length = self.length + 1
        
class Node:                               # a helper
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)
        
    def print_backward(self):
		if self.next != None:
			tail = self.next
			tail.print_backward()
		print self.cargo,



# exercise
def print_list(node):
    s = '['
    while node:
        s += str(node.cargo)
        node = node.next
        if node:
            s += ', '
    s += ']'
    print s

print_list(node1)                          # [1, 2, 3]
