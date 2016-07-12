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
