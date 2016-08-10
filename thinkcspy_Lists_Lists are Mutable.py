alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = []
print(alist)


alist = ['a', 'd', 'f']
alist[1:1] = ['b', 'c']
print(alist)
alist[4:4] = ['e']
print(alist)
