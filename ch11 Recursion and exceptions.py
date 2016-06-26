#Example1:swap
a=1
b=2
#~ def swap(x, y):      # incorrect version
	#~ x,y= y, x
	#~ return (x,y)
#~ 
#~ swap(a, b)

def swap(x, y):
	return y, x
a,b=swap(a,b)
print a,b

#Example2
def encapsulate(val, seq):
	if type(seq) == type(""):
		return str(val)
	if type(seq) == type([]):
		return [val]
	return (val,)
def insert_in_middle(val, seq):
	middle = len(seq)/2
	return seq[:middle] + encapsulate(val, seq) + seq[middle:]

my_string = 'abde'
my_list = ['a', 'b', 'd', 'e']
my_tuple = ('a', 'b', 'd', 'e')
print insert_in_middle('c', my_string)     #'abcde'
print insert_in_middle('c', my_list)       #['a', 'b', 'c', 'd', 'e']
print insert_in_middle('c', my_tuple)      #('a', 'b', 'c', 'd', 'e')

#Example3:recursive
def recursive_max(nested_num_list):
	"""
	  >>> recursive_max([2, 9, [1, 13], 8, 6])
	  13
	  >>> recursive_max([2, [[100, 7], 90], [1, 13], 8, 6])
	  100
	  >>> recursive_max([2, [[13, 7], 90], [1, 100], 8, 6])
	  100
	  >>> recursive_max([[[13, 7], 90], 2, [1, 100], 8, 6])
	  100
	"""
	largest = 0
	for element in nested_num_list:
		if type(element) == type([]):
			sub_largest=recursive_max(element)
			if largest<sub_largest:
				largest=sub_largest
		else:
			if largest<element:
				largest=element
	return largest
if __name__ == '__main__':
	import doctest
	doctest.testmod()


#Example4:exception and raise error
def exists(filename):
	try:
		f = open(filename)
		f.close()
		return True
	except:
		return False
print exists('111')

#~ def get_age(age):
	#~ if age < 0:
		#~ raise ValueError, '%s is not a valid age' % age
	#~ return age
#~ get_age(-2)


#Example5:list comprehension
numbers = [1, 2, 3, 4]
print [x**2 for x in numbers]                                           #[1, 4, 9, 16]
print [x**2 for x in numbers if x**2 > 8]                               #[9, 16]
print [(x, x**2, x**3) for x in numbers]                                #[(1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64)]
letters = ['a', 'b', 'c']
print [n*letter for n in numbers for letter in letters]                 #['a', 'b', 'c', 'aa', 'bb', 'cc', 'aaa', 'bbb', 'ccc', 'aaaa', 'bbbb', 'cccc']


#6.tree
#!/usr/bin/env python

import os
import sys

def getroot():
	if len(sys.argv) == 1:  #sys.argv is the list of command-line arguments. len(sys.argv) is the number of command-line arguments.
		path = ''
	else:
		path = sys.argv[1]  #get the first argument after the script for a filename

	if os.path.isabs(path): #absolute path
		tree_root = path
	else:
		tree_root = os.path.join(os.getcwd(), path)   #returns current working directory of a process + path

	return tree_root


def getdirlist(path):
	dirlist = os.listdir(path)   #returns a list containing the names of the entries in the directory given by path
	dirlist = [name for name in dirlist if name[0] != '.']  #omit '.'
	dirlist.sort()
	return dirlist


def traverse(path, prefix='|--', s='.\n', f=0, d=0):
	dirlist = getdirlist(path)

	for num, file in enumerate(dirlist):
		lastprefix = prefix[:-3] + '`--'            #prefix='|--',lastprefix='`--'
		dirsize = len(dirlist)

		if num < dirsize - 1:
			s += '%s %s\n' % (prefix, file)         #pres='|-- 123.txt',lasts='`-- 456.txt'
		else:
			s += '%s %s\n' % (lastprefix, file)
		path2file = os.path.join(path, file)        #path join file(find subdirectory!!!)

		if os.path.isdir(path2file):                #return True if that path exists and is a directory
			d += 1
			if getdirlist(path2file):               #return True if subdirectory is not empty
				s, f, d = traverse(path2file, '|   ' + prefix, s, f, d) #path recursion(open subdirectory!!!)
		else:
			f += 1

	return s, f, d


if __name__ == '__main__':
	root = getroot()
	tree_str, files, dirs = traverse(root)

	if dirs == 1:
		dirstring = 'directory'
	else:
		dirstring = 'directories'
	if files == 1:
		filestring = 'file'
	else:
		filestring = 'files'

	print tree_str
	print '%d %s, %d %s' % (dirs, dirstring, files, filestring)


#1.tuple
def make_empty(seq):
	"""
	  >>> make_empty([1, 2, 3, 4])
	  []
	  >>> make_empty(('a', 'b', 'c'))
	  ()
	  >>> make_empty("No, not me!")
	  ''
	"""
	if type(seq) == type([]):
		return []
	if type(seq) == type(()):
		return ()
	return ''
	
	
def insert_at_end(val, seq):
	"""
	  >>> insert_at_end(5, [1, 3, 4, 6])
	  [1, 3, 4, 6, 5]
	  >>> insert_at_end('x', 'abc')
	  'abcx'
	  >>> insert_at_end(5, (1, 3, 4, 6))
	  (1, 3, 4, 6, 5)
	"""
	if type(seq) == type([]):
		return seq+[val]
	if type(seq) == type(()):
		return seq+(val,)
	return seq+val


def insert_in_front(val, seq):
	"""
	  >>> insert_in_front(5, [1, 3, 4, 6])
	  [5, 1, 3, 4, 6]
	  >>> insert_in_front(5, (1, 3, 4, 6))
	  (5, 1, 3, 4, 6)
	  >>> insert_in_front('x', 'abc')
	  'xabc'
	"""
	if type(seq) == type([]):
		return [val]+seq
	if type(seq) == type(()):
		return (val,)+seq
	return val+seq
	

def index_of(val, seq, start=0):
	"""
	  >>> index_of(9, [1, 7, 11, 9, 10])
	  3
	  >>> index_of(5, (1, 2, 4, 5, 6, 10, 5, 5))
	  3
	  >>> index_of(5, (1, 2, 4, 5, 6, 10, 5, 5), 4)
	  6
	  >>> index_of('y', 'happy birthday')
	  4
	  >>> index_of('banana', ['apple', 'banana', 'cherry', 'date'])
	  1
	  >>> index_of(5, [2, 3, 4])
	  -1
	  >>> index_of('b', ['apple', 'banana', 'cherry', 'date'])
	  -1
	"""
	for i in range(start, len(seq)):
		if seq[i] == val:
			return i
	return -1


def remove_at(index, seq):
	"""
	  >>> remove_at(3, [1, 7, 11, 9, 10])
	  [1, 7, 11, 10]
	  >>> remove_at(5, (1, 4, 6, 7, 0, 9, 3, 5))
	  (1, 4, 6, 7, 0, 3, 5)
	  >>> remove_at(2, "Yomrktown")
	  'Yorktown'
	"""
	return seq[:index] + seq[index + 1:]
		
		
def remove_val(val, seq):
	"""
	  >>> remove_val(11, [1, 7, 11, 9, 10])
	  [1, 7, 9, 10]
	  >>> remove_val(15, (1, 15, 11, 4, 9))
	  (1, 11, 4, 9)
	  >>> remove_val('what', ('who', 'what', 'when', 'where', 'why', 'how'))
	  ('who', 'when', 'where', 'why', 'how')
	"""
	return remove_at(index_of(val, seq), seq)


def remove_all(val, seq):
	"""
	  >>> remove_all(11, [1, 7, 11, 9, 11, 10, 2, 11])
	  [1, 7, 9, 10, 2]
	  >>> remove_all('i', 'Mississippi')
	  'Msssspp'
	"""
	while index_of(val, seq) != -1:
		seq = remove_val(val, seq)
	return seq


def count(val, seq):
	"""
	  >>> count(5, (1, 5, 3, 7, 5, 8, 5))
	  3
	  >>> count('s', 'Mississippi')
	  4
	  >>> count((1, 2), [1, 5, (1, 2), 7, (1, 2), 8, 5])
	  2
	"""
	count = 0
	for item in seq:
		if item == val:
			count += 1
	return count
	

def reverse(seq):
	"""
	  >>> reverse([1, 2, 3, 4, 5])
	  [5, 4, 3, 2, 1]
	  >>> reverse(('shoe', 'my', 'buckle', 2, 1))
	  (1, 2, 'buckle', 'my', 'shoe')
	  >>> reverse('Python')
	  'nohtyP'
	"""
	output = make_empty(seq)
	for item in seq:
		output = insert_in_front(item, output)
	return output


def sort_sequence(seq):
	"""
	  >>> sort_sequence([3, 4, 6, 7, 8, 2])
	  [2, 3, 4, 6, 7, 8]
	  >>> sort_sequence((3, 4, 6, 7, 8, 2))
	  (2, 3, 4, 6, 7, 8)
	  >>> sort_sequence("nothappy")
	  'ahnoppty'
	"""
	new_list=list(seq)
	new_list.sort()                              #list.sort()
	output = make_empty(seq)
	for item in new_list:
		output = insert_at_end(item, output)
	return output

if __name__ == "__main__":
	import doctest
	doctest.testmod()


#2.min
def recursive_min(nested_num_list):
	"""
	  >>> recursive_min([2, 9, [1, 13], 8, 6])
	  1
	  >>> recursive_min([2, [[100, 1], 90], [10, 13], 8, 6])
	  1
	  >>> recursive_min([2, [[13, -7], 90], [1, 100], 8, 6])
	  -7
	  >>> recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6])
	  -13
	"""
	minimum = nested_num_list[0]
	while type(minimum) == type([]):
		minimum = minimum[0]
	for element in nested_num_list:
		if type(element) == type([]):
			minimum_of_element = recursive_min(element)
			if minimum > minimum_of_element:
				minimum = minimum_of_element
		else:
			if minimum > element:
				minimum = element
	return minimum

if __name__ == "__main__":
	import doctest
	doctest.testmod()


#3.count
def recursive_count(target, nested_num_list):
	"""
	  >>> recursive_count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]])
	  4
	  >>> recursive_count(7, [[9, [7, 1, 13, 2], 8], [7, 6]])
	  2
	  >>> recursive_count(15, [[9, [7, 1, 13, 2], 8], [2, 6]])
	  0
	  >>> recursive_count(5, [[5, [5, [1, 5], 5], 5], [5, 6]])
	  6
	"""
	count=0
	for element in nested_num_list:
		if type(element) == type([]):
			count+=recursive_count(target, element)
		else:
			if target==element:
				count+=1
	return count

if __name__ == "__main__":
	import doctest
	doctest.testmod()


#4.flatten
def flatten(nested_num_list):
	"""
	  >>> flatten([2, 9, [2, 1, 13, 2], 8, [2, 6]])
	  [2, 9, 2, 1, 13, 2, 8, 2, 6]
	  >>> flatten([[9, [7, 1, 13, 2], 8], [7, 6]])
	  [9, 7, 1, 13, 2, 8, 7, 6]
	  >>> flatten([[9, [7, 1, 13, 2], 8], [2, 6]])
	  [9, 7, 1, 13, 2, 8, 2, 6]
	  >>> flatten([[5, [5, [1, 5], 5], 5], [5, 6]])
	  [5, 5, 1, 5, 5, 5, 5, 6]
	"""
	l=[]
	for element in nested_num_list:
		if type(element) == type([]):
			l+=flatten(element)
		else:
			l+=[element]
	return l

if __name__ == "__main__":
	import doctest
	doctest.testmod()


#5.raise error
def readposint(prompt = 'Please enter a positive integer: '):
    while True:
		posint = raw_input(prompt)
		posint = float(posint)
		if posint != int(posint):
			raise ValueError, '%s is not an integer' % posint
		elif posint <= 0:
			raise ValueError, '%s is not positive' % posint
		break
            
    return int(posint)
    
readposint()


#6.list
nums = [1, 2, 3, 4]
print [x**3 for x in nums]
nums = [1, 2, 3, 4]
print [x**2 for x in nums if x**2 != 4]
nums = [1, 2, 3, 4]
print [(x, y) for x in nums for y in nums]
nums = [1, 2, 3, 4]
print [(x, y) for x in nums for y in nums if x != y]


#7.factorial
def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a
print f(5)
