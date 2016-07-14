# Example1: Building trees
class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.cargo)
        
tree = Tree(1, Tree(2), Tree(3))


# Example2: Traversing trees
def total(tree):
    if tree == None: return 0
    return total(tree.left) + total(tree.right) + tree.cargo
    
    
# Example3: Expression trees
tree = Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))


# Example4: Tree traversal
def print_tree(tree):
    if tree == None: return
    print tree.cargo,
    print_tree(tree.left)
    print_tree(tree.right)

tree = Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))    # prefix
print_tree(tree)                                          #~ + 1 * 2 3

print

def print_tree_postorder(tree):
    if tree == None: return
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print tree.cargo,
    
tree = Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))    # profix
print_tree_postorder(tree)                                # 1 2 3 * +

print

def print_tree_inorder(tree):
    if tree == None: return
    print_tree_inorder(tree.left)
    print tree.cargo,
    print_tree_inorder(tree.right)
    
tree = Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))    # inorder
print_tree_inorder(tree)                                  # 1 + 2 * 3

print



def print_tree_indented(tree, level=0):
    if tree == None: return
    print_tree_indented(tree.right, level+1)
    print '  ' * level + str(tree.cargo)
    print_tree_indented(tree.left, level+1)
    
print_tree_indented(tree)
    #~ 3
  #~ *
    #~ 2
#~ +
  #~ 1


# Example5: Building an expression tree
def get_token(token_list, expected):  # 1.get token
    if token_list[0] == expected:
        del token_list[0]
        return True
    else:
        return False

        
def get_number(token_list):            # 2.get number
    x = token_list[0]
    if type(x) != type(0): return None
    del token_list[0]
    return Tree (x, None, None)        # if the token is a number, removes it and returns a leaf node containing the number
    
token_list = [9, 11, 'end']
x = get_number(token_list)
print_tree_postorder(x)                # 9
print token_list                       # [11, 'end']


def get_product(token_list):           # 3.get product
    a = get_number(token_list)
    if get_token(token_list, '*'):
        b = get_number(token_list)
        return Tree ('*', a, b)
    else:
        return a
        
token_list = [9, '*', 11, 'end']
tree = get_product(token_list)
print_tree_postorder(tree)             # 9 11 *

token_list = [9, '+', 11, 'end']
tree = get_product(token_list)
print_tree_postorder(tree)             # 9

print

def get_product(token_list):           # 4.modify product
    a = get_number(token_list)
    if get_token(token_list, '*'):
        b = get_product(token_list)    # this line changed, recursion
        return Tree ('*', a, b)
    else:
        return a
        
token_list = [2, '*', 3, '*', 5 , '*', 7, 'end']
tree = get_product(token_list)
print_tree_postorder(tree)             # 2 3 5 7 * * *

print

def get_sum(token_list):               # 5.sum
    a = get_product(token_list)
    if get_token(token_list, '+'):
        b = get_sum(token_list)        # recursion
        return Tree ('+', a, b)
    else:
        return a
        
token_list = [9, '*', 11, '+', 5, '*', 7, 'end']
tree = get_sum(token_list)
print_tree_postorder(tree)             # 9 11 * 5 7 * +

print

def get_number(token_list):            # 6.modify get number
    if get_token(token_list, '('):
        x = get_sum(token_list)        # get the subexpression
        get_token(token_list, ')')     # remove the closing parenthesis
        return x
    else:
        x = token_list[0]
        if type(x) != type(0): return None
        token_list[0:1] = []
        return Tree (x, None, None)

token_list = [9, '*', '(', 11, '+', 5, ')', '*', 7, 'end']
tree = get_sum(token_list)
print_tree_postorder(tree)             # 9 11 5 + 7 * *

print

# Example6: Handling errors
def get_number(token_list):
    if get_token(token_list, '('):
        x = get_sum(token_list)
        if not get_token(token_list, ')'):
            raise 'BadExpressionError', 'missing parenthesis'
        return x
    else:
        x = token_list[0]
        if type(x) != type(0): return None
        token_list[0:1] = []
        return Tree (x, None, None)


# Example7: The animal tree
def yes(ques):
    ans = raw_input(ques).lower()
    return ans[0] == 'y'

def animal():
    # start with a singleton
    root = Tree("bird")

    # loop until the user quits
    while True:
        print
        if not yes("Are you thinking of an animal? "): break

        # walk the tree
        tree = root
        while tree.left != None:
            prompt = tree.cargo + "? "
            if yes(prompt):
                tree = tree.right
            else:
                tree = tree.left

        # make a guess
        guess = tree.cargo
        prompt = "Is it a " + guess + "? "
        if yes(prompt):
            print "I rule!"
            continue

        # get new information
        prompt  = "What is the animal's name? "
        animal  = raw_input(prompt)
        prompt  = "What question would distinguish a %s from a %s? "
        question = raw_input(prompt % (animal, guess))

        # add new information to the tree
        tree.cargo = question
        prompt = "If the animal were %s the answer would be? "
        if yes(prompt % animal):
            tree.left = Tree(guess)
            tree.right = Tree(animal)
        else:
            tree.left = Tree(animal)
            tree.right = Tree(guess)
            
            
# 1.modify print_tree_inorder
def print_tree_inorder(tree):
    if tree == None: return
    if tree.left:
        print '(',
    print_tree_inorder(tree.left),
    print tree.cargo,
    print_tree_inorder(tree.right),
    if tree.right:
        print ')',

token_list =['(',3, '+', 7, ')', '*', '(', 5, '+', 3, ')', '+', 4, '*', 5, 'end']
tree = get_sum(token_list)
print_tree_inorder(tree)     # ( ( ( 3 + 7 ) * ( 5 + 3 ) ) + ( 4 * 5 ) )


# 2.a function that takes an expression string and returns a token list
def make_token_list(s):
    token_list = []
    for char in s:
        if char == ' ':
            continue
        elif char.isdigit():
            token_list.append(int(char))
        else:
            token_list.append(char)
    token_list.append('end')
    return token_list


# 3.save the animal knowledge tree in a file(???)
def dump(tree):                  
    # returns string representation of tree in postfix-style
    # order with commas separating nodes. Leaves are
    # represented with two preceding commas, corresponding to
    # the empty tree.left & tree.right attributes.
    if tree == None: return ','  
    s = ''                       
    s += dump(tree.left)        
    s += dump(tree.right)
    s += str(tree) + ','   
    return s

def restore_tree(token_list):
    # Recreate tree from token list generated from save file
    cargo = token_list.pop()
    if cargo == '': return
    right = restore_tree(token_list)
    left = restore_tree(token_list)
    tree = Tree(cargo, left, right)
    return tree

def animal():
    #start with a singleton
    root = Tree("bird")

    # or use save file if it exists
    try:
        infile = open(savefile, 'r')
        s = infile.read()
        infile.close()
        token_list = s.split(',')
        token_list.pop() #remove empty item at end
        root = restore_tree(token_list)
    except IOError: 
        pass
    
    # loop until the user quits
    while True:
        print
        if not yes("Are you thinking of an animal? "): break

        # walk the tree
        tree = root
        while tree.left != None:
            prompt = tree.cargo + "? "
            if yes(prompt):
                tree = tree.right
            else:
                tree = tree.left

        # make a guess
        guess = tree.cargo
        prompt = "Is it a " + guess + "? "
        if yes(prompt):
            print "Yatta!"
            continue

        # get new information
        prompt  = "What is the animal's name? "
        animal  = raw_input(prompt)
        prompt  = "What question would distinguish a %s from a %s? "
        question = raw_input(prompt % (animal, guess)).strip('?').capitalize()

        # add new information to the tree
        tree.cargo = question
        prompt = "If the animal were %s the answer would be? "
        if yes(prompt % animal):
            tree.left = Tree(guess)
            tree.right = Tree(animal)
        else:
            tree.left = Tree(animal)
            tree.right = Tree(guess)

    # save the tree
    s = dump(root)
    outfile = open(savefile, 'w')
    outfile.write(s)
    outfile.close()
