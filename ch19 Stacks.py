class Stack :
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()     # remove and return an item(the last one that was added) from the stack

    def is_empty(self):
        return (self.items == [])
        
        
s = Stack()
s.push(54)
s.push(45)
s.push("+")
while not s.is_empty():
    print s.pop(),                 # + 45 54



import re
re.split("([^0-9])", "123+456*/")  # the delimiter comes before the string, [^0-9] is the set of everything that is not a number
# ['123', '+', '456', '*', '', '/', '']



def eval_postfix(expr):
    import re
    token_list = re.split("([^0-9])", expr)
    stack = Stack()
    for token in token_list:
        if  token == '' or token == ' ':
            continue
        if  token == '+':
            sum = stack.pop() + stack.pop()
            stack.push(sum)
        elif token == '*':
            product = stack.pop() * stack.pop()
            stack.push(product)
        else:
            stack.push(int(token))
    return stack.pop()

print eval_postfix ("56 47 + 2 *")  # 206



# exercise
# (1 + 2) * 3
print eval_postfix("1 2 + 3 *")     # 9

# 1 + 2 * 3
print eval_postfix("1 2 3 * +")     # 7
