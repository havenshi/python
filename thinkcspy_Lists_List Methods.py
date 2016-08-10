a = ['one', 'two', 'three']
del a[1]
print(a)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
del alist[1:5]
print(alist)



mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist.insert(1, 12)
print(mylist)
print(mylist.count(12))

print(mylist.index(3))
print(mylist.count(5))

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

mylist.remove(5)
print(mylist)

lastitem = mylist.pop()
print(lastitem)
print(mylist)


#~ [5, 27, 3, 12]
#~ [5, 12, 27, 3, 12]
#~ 2
#~ 3
#~ 1
#~ [12, 3, 27, 12, 5]
#~ [3, 5, 12, 12, 27]
#~ [3, 12, 12, 27]
#~ 27
#~ [3, 12, 12]

# It is important to remember that methods like append, sort, and reverse all return None. 
