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


#Example4:exception
def exists(filename):
    try:
        f = open(filename)
        f.close()
        return True
    except:
        return False
print exists('111')

def get_age(age):
    if age < 0:
        raise ValueError, '%s is not a valid age' % age
    return age
get_age(-2)

print 2
