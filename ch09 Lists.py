#Example1:false
if {} or [] or () or None or 0:
	print 'This is true.'
else:
	print 'This is false.'

#Example2:copy cand cloning
a = [1, 2, 3]
b = a
print a is b   #True
b[0] = 5
print a        #[5, 2, 3]

c = [1, 2, 3]
d = c[:]
print c is d   #False
d[0] = 5
print d        #[1, 2, 3]


e = "banana"
f = "banana"
print e is f    #True

#Example3:function(not pure)

numbers = [1, 2, 3, 4, 5]

for index, value in enumerate(numbers):
	numbers[index] = value**2
	print numbers

#Example4:matrix
print [0]*3      #one []
print [[0]*3]*5  #don't forget the second []
print ([0]*3)*5  #omit ()
print [(0)*3]*5  #omit ()
print [0,0]*3    #[]
print (0,0)*3    #()

def make_matrix(rows, columns):
	matrix = []
	for row in range(rows):
		matrix += [[0] * columns]
	return matrix

m = make_matrix(4, 3)
m[1][2] = 7
print m   #[[0, 0, 0], [0, 0, 7], [0, 0, 0], [0, 0, 0]]


import string

char_list = list("Frog")
print string.join(char_list, ' ')


#1.loop
l=['spam!', 'one', ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
for i in range(len(l)):
	print len(l[i])

#2.list
"""
  >>> a_list[3]
  42
  >>> a_list[6]
  'Ni!'
  >>> len(a_list)
  8
"""
a_list = [1, 2, 3, 42, 5, 6, 'Ni!', 8]

if __name__ == '__main__':
	import doctest
	doctest.testmod()
	
"""
  >>> b_list[1:]
  ['Stills', 'Nash']
  >>> group = b_list + c_list
  >>> group[-1]
  'Young'
"""
b_list = ['Crosby', 'Stills', 'Nash'] 
c_list = ['Younga']

if __name__ == '__main__':
	import doctest
	doctest.testmod()

"""
  >>> 'war' in mystery_list
  False
  >>> 'peace' in mystery_list
  True
  >>> 'justice' in mystery_list
  True
  >>> 'oppression' in mystery_list
  False
  >>> 'equality' in mystery_list
  True
"""
mystery_list = ['peace', 'justice', 'equality']

if __name__ == '__main__':
	import doctest
	doctest.testmod()
	
"""
  >>> range(a, b, c)
  [5, 9, 13, 17]
"""
a = 5
b = 18
c = 4

if __name__ == '__main__':
	import doctest
	doctest.testmod()

#3.range
print range(10, 0, -2)

#4.clone
a = [1, 2, 3]
b = a[:]
b[0] = 5
print b,a

#5.%
this = ['I', 'am', 'not', 'a', 'crook']
that = ['I', 'am', 'not', 'a', 'crook']
print "Test 1: %s" % (this is that)
that = this
print "Test 2: %s" % (this is that)

#6.list test
"""
  >>> 13 in junk
  True
  >>> del junk[4]
  >>> junk
  [3, 7, 9, 10, 17, 21, 24, 27]
  >>> del junk[a:b]
  >>> junk
  [3, 7, 27]
"""
junk = [3, 7, 9, 10, 13, 17, 21, 24, 27]
a = 2
b = (len(junk) - 2)

if __name__ == '__main__':
	import doctest
	doctest.testmod()

"""
  >>> nlist[2][1]
  0
  >>> nlist[0][2]
  17
  >>> nlist[1][1]
  5
"""
nlist = [[1, 2, 17], [4, 5, 6], [7, 0, 9]]

if __name__ == '__main__':
	import doctest
	doctest.testmod()

"""
  >>> import string
  >>> string.split(message, '??')
  ['this', 'and', 'that']
"""
message = "this??and??that"

if __name__ == '__main__':
	import doctest
	doctest.testmod()

#7.vector
def add_vectors(u, v):
	"""
	  >>> add_vectors([1, 0], [1, 1])
	  [2, 1]
	  >>> add_vectors([1, 2], [1, 4])
	  [2, 6]
	  >>> add_vectors([1, 2, 1], [1, 4, 3])
	  [2, 6, 4]
	  >>> add_vectors([11, 0, -4, 5], [2, -4, 17, 0])
	  [13, -4, 13, 5]
	"""
	new_list=[]
	for i,value in enumerate(u):
		new_list+=[u[i]+v[i]]
	return new_list
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()

#8.multiple
def scalar_mult(s, v):
	"""
	  >>> scalar_mult(5, [1, 2])
	  [5, 10]
	  >>> scalar_mult(3, [1, 0, -1])
	  [3, 0, -3]
	  >>> scalar_mult(7, [3, 0, 5, 11, 2])
	  [21, 0, 35, 77, 14]
	"""
	new_list=[]
	for i,value in enumerate(v):
		new_list+=[s*v[i]]
	return new_list
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()

#9.product
def dot_product(u, v):
	"""
	  >>> dot_product([1, 1], [1, 1])
	  2
	  >>> dot_product([1, 2], [1, 4])
	  9
	  >>> dot_product([1, 2, 1], [1, 4, 3])
	  12
	  >>> dot_product([2, 0, -1, 1], [1, 5, 2, 0])
	  0
	"""
	origin=0
	for i,value in enumerate(u):
		origin+=u[i]*v[i]
	return origin
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()

#10.cross product
def dot_product(u, v):
	"""
	  >>> dot_product([1, 2, 3], [1, 2, 3])
	  11
	  >>> dot_product([1, 6, 8], [1, 2, 4])
	  34
	  >>> dot_product([1, 2, 1], [1, 4, 0])
	  5
	  >>> dot_product([2, 0, -1], [1, 5, 2])
	  9
	"""
	origin=0
	for i,value in enumerate(u):
		if i<len(u)-1:
			origin+=u[i]*v[i+1]
		else:
			origin+=u[i]*v[0]
	return origin
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()

#11.matrix
def add_row(matrix):
	"""
	  >>> m = [[0, 0], [0, 0]]
	  >>> add_row(m)
	  [[0, 0], [0, 0], [0, 0]]
	  >>> n = [[3, 2, 5], [1, 4, 7]]
	  >>> add_row(n)
	  [[3, 2, 5], [1, 4, 7], [0, 0, 0]]
	  >>> n
	  [[3, 2, 5], [1, 4, 7]]
	"""
	extra=[[0]*len(matrix[0])]
	return matrix+extra
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()

def add_column(matrix):
	"""
	  >>> add_column([[0, 0], [0, 0]])
	  [[0, 0, 0], [0, 0, 0]]
	  >>> add_column([[3, 2], [5, 1], [4, 7]])
	  [[3, 2, 0], [5, 1, 0], [4, 7, 0]]
	"""
	matrix1= matrix[:]
	for i in range(len(matrix)):
		matrix1[i]+=[0]
	return matrix1
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()
	
#12.add matrices
def add_matrices(m1, m2):
	"""
	  >>> a = [[1, 2], [3, 4]]
	  >>> b = [[2, 2], [2, 2]]
	  >>> add_matrices(a, b)
	  [[3, 4], [5, 6]]
	  >>> c = [[8, 2], [3, 4], [5, 7]]
	  >>> d = [[3, 2], [9, 2], [10, 12]]
	  >>> add_matrices(c, d)
	  [[11, 4], [12, 6], [15, 19]]
	  >>> c
	  [[8, 2], [3, 4], [5, 7]]
	  >>> d
	  [[3, 2], [9, 2], [10, 12]]
	"""
	new_matrix=[]
	for i,row in enumerate(m1):
		new_row=[]
		for j,value in enumerate(row):
			new_row+=[m1[i][j]+m2[i][j]]
		new_matrix+=[new_row]
	return new_matrix
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()

#13.multiple
def scalar_mult(s, m):
	"""
	  >>> a = [[1, 2], [3, 4]]
	  >>> scalar_mult(3, a)
	  [[3, 6], [9, 12]]
	  >>> b = [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
	  >>> scalar_mult(10, b)
	  [[30, 50, 70], [10, 10, 10], [0, 20, 0], [20, 20, 30]]
	  >>> b
	  [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
	"""
	new_matrix=[]
	for i,row in enumerate(m):
		new_row=[]
		for j,value in enumerate(row):
			new_row+=[s*m[i][j]]
		new_matrix+=[new_row]
	return new_matrix
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()
	
#14.row times column and matrix mult
def row_times_column(m1, row, m2, column):
	"""
	  >>> row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 0)
	  19
	  >>> row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 1)
	  22
	  >>> row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 0)
	  43
	  >>> row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 1)
	  50
	"""
	m=0
	i=0
	for a in m1[row]:
		if i<len(m1[0]):
			m+=a*(m2[i][column])
		i+=1
	return m
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()
	
def matrix_mult(m1, m2):
	"""
	  >>> matrix_mult([[1, 2], [3,  4]], [[5, 6], [7, 8]])
	  [[19, 22], [43, 50]]
	  >>> matrix_mult([[1, 2, 3], [4,  5, 6]], [[7, 8], [9, 1], [2, 3]])
	  [[31, 19], [85, 55]]
	  >>> matrix_mult([[7, 8], [9, 1], [2, 3]], [[1, 2, 3], [4, 5, 6]])
	  [[39, 54, 69], [13, 23, 33], [14, 19, 24]]
	"""
	new_matrix=[]
	for i in range(len(m1)):
		new_row=[]
		for j in range(len(m2[0])):
			new_row+=[row_times_column(m1, i, m2, j)]
		new_matrix+=[new_row]
	return new_matrix
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()

#15.numberlist
def only_evens(numbers):
	"""
	  >>> only_evens([1, 3, 4, 6, 7, 8])
	  [4, 6, 8]
	  >>> only_evens([2, 4, 6, 8, 10, 11, 0])
	  [2, 4, 6, 8, 10, 0]
	  >>> only_evens([1, 3, 5, 7, 9, 11])
	  []
	  >>> only_evens([4, 0, -1, 2, 6, 7, -4])
	  [4, 0, 2, 6, -4]
	  >>> nums = [1, 2, 3, 4]
	  >>> only_evens(nums)
	  [2, 4]
	  >>> nums
	  [1, 2, 3, 4]
	"""
	new_list=[]
	for i in range(len(numbers)):
		if numbers[i]%2==0:
			new_list+=[numbers[i]]
	return new_list
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()


def only_odds(numbers):
	"""
	  >>> only_odds([1, 3, 4, 6, 7, 8])
	  [1, 3, 7]
	  >>> only_odds([2, 4, 6, 8, 10, 11, 0])
	  [11]
	  >>> only_odds([1, 3, 5, 7, 9, 11])
	  [1, 3, 5, 7, 9, 11]
	  >>> only_odds([4, 0, -1, 2, 6, 7, -4])
	  [-1, 7]
	  >>> nums = [1, 2, 3, 4]
	  >>> only_odds(nums)
	  [1, 3]
	  >>> nums
	  [1, 2, 3, 4]
	"""
	new_list=[]
	for i in range(len(numbers)):
		if numbers[i]%2!=0:
			new_list+=[numbers[i]]
	return new_list
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()

#16.multiple of num and numlist
def multiples_of(num, numlist):
	"""
		>>> multiples_of(2,[1, 2, 3, 4])
		[2, 4]
		>>> multiples_of(3,[1, 2, 3, 4, 5, 6])
		[3, 6]
	"""
	result = []
	for i in range(len(numlist)):
		if numlist[i] % num == 0:
			result+=[numlist[i]]
	return result
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()

#17.join and split
import string

song = "The rain in Spain..."
print string.split(song)
print string.join(string.split(song))

#18.replace
def replace(s, old, new):
	"""
	  >>> replace('Mississippi', 'i', 'I')
	  'MIssIssIppI'
	  >>> s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
	  >>> replace(s, 'om', 'am')
	  'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!'
	  >>> replace(s, 'o', 'a')
	  'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!'
	"""
	new_list=string.split(s,old)
	return string.join(new_list,new)
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()
