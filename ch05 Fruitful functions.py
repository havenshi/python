#1.compare
def compare(a, b):
	"""
		>>> compare(5, 4)
		1
		>>> compare(7, 7)
		0
		>>> compare(2, 3)
		-1
		>>> compare(42, 1)
		1
	"""
	
	if a > b:
		return 1
	elif a == b:
		return 0
	else:
		return -1
		
if __name__ == '__main__':
	import doctest
	doctest.testmod()

#2.length of the hypotenuse of a right triangle
def hypotenuse(a, b):
	"""
	  >>> hypotenuse(3, 4)
	  5.0
	  >>> hypotenuse(12, 5)
	  13.0
	  >>> hypotenuse(7, 24)
	  25.0
	  >>> hypotenuse(9, 12)
	  15.0
	"""
	return float((a**2+b**2)**0.5)

if __name__ == '__main__':
	import doctest
	doctest.testmod()

#3.slope and intercept
def slope(x1, y1, x2, y2):
	"""
	  >>> slope(5, 3, 4, 2)
	  1.0
	  >>> slope(1, 2, 3, 2)
	  0.0
	  >>> slope(1, 2, 3, 3)
	  0.5
	  >>> slope(2, 4, 1, 2)
	  2.0
	"""
	return float(abs((y2-y1)*100/(x2-x1)))/100
	
def intercept(x1, y1, x2, y2):
	"""
	  >>> intercept(1, 6, 3, 12)
	  3.0
	  >>> intercept(6, 1, 1, 6)
	  7.0
	  >>> intercept(4, 6, 12, 8)
	  5.0
	"""
	return float(x2*y1-x1*y2)/(x2-x1)
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()

#4.even
def is_even(n):
	'''
	  >>> is_even(2)
	  True
	  >>> is_even(3)
	  False
	'''
	if n%2==0:
		return True
	else:
		return False
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()

#5.odd
def is_odd(n):
	'''
	  >>> is_odd(5)
	  True
	  >>> is_odd(6)
	  False
	'''
	if is_even(n)==True:
		return False
	else:
		return True

if __name__ == '__main__':
	import doctest
	doctest.testmod()

#6.factor
def is_factor(f, n):
	"""
	  >>> is_factor(3, 12)
	  True
	  >>> is_factor(5, 12)
	  False
	  >>> is_factor(7, 14)
	  True
	  >>> is_factor(2, 14)
	  True
	  >>> is_factor(7, 15)
	  False
	"""
	if n%f==0:
		return True
	else:
		return False
		
if __name__ == '__main__':
	import doctest
	doctest.testmod()

#7.multiple
def is_multiple(m, n):
	"""
	  >>> is_multiple(12, 3)
	  True
	  >>> is_multiple(12, 4)
	  True
	  >>> is_multiple(12, 5)
	  False
	  >>> is_multiple(12, 6)
	  True
	  >>> is_multiple(12, 7)
	  False
	"""
	if m%n==0:
		return True
	else:
		return False

if __name__ == '__main__':
	import doctest
	doctest.testmod()

#8.convert Fahrenheit to Celsius
def f2c(t):
	"""
	  >>> f2c(212)
	  100
	  >>> f2c(32)
	  0
	  >>> f2c(-40)
	  -40
	  >>> f2c(36)
	  2
	  >>> f2c(37)
	  3
	  >>> f2c(38)
	  3
	  >>> f2c(39)
	  4
	"""
	return (int(round((t-32)*500/9,-2)))/100
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()

#9.convertCelsius to Fahrenheit
def c2f(t):
	"""
	  >>> c2f(0)
	  32
	  >>> c2f(100)
	  212
	  >>> c2f(-40)
	  -40
	  >>> c2f(12)
	  54
	  >>> c2f(18)
	  64
	  >>> c2f(-48)
	  -54
	"""
	return int(round(t*180+3200,-2))/100
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()
