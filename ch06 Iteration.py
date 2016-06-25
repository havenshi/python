#Example1
def num_digits(n):
	count = 0
	while n:
		if n%10==0 or n%10==5:
			count=count+1
		n=n/10
	return count
	
print(num_digits(1055030250))

#Example2
x = 1
while x < 13:
	print x, '\t', 2**x
	x += 1

#Example3
def print_multiples(n):
	i = 1
	while i <= n:
		j=1
		while j<=n:
			print j * i, '\t',
			j += 1		
		print
		i+=1
	
print_multiples(5)

def print_multiples_half(n):
	i = 1
	while i <= n:
		j=1
		while j<=i:
			print j * i, '\t',
			j += 1		
		print
		i+=1
	
print_multiples_half(5)

#1.write a single string
print '''produces
this
output.'''

#2.square root
def sqrt(n):
	approx = n/2.0
	better = (approx + n/approx)/2.0
	while better != approx:
		approx = better
		better = (approx + n/approx)/2.0
	return approx,better
print sqrt(25)

#3.triangular numbers
def print_triangular_numbers(n):
	i=1
	while i<=n:
		print i,'\t',(1+i)*i/2
		i+=1
print_triangular_numbers(5)

#4.prime
def is_prime(n):
	'''
	  >>> is_prime(3)
	  True
	  >>> is_prime(5)
	  True
	  >>> is_prime(9)
	  False
	  >>> is_prime(15)
	  False
	  >>> is_prime(17)
	  True
	  >>> is_prime(21)
	  False
	'''
	i=2
	while i<n:
		if n%i==0:
			return False
			break
		i+=1
	return True
if __name__ == '__main__':
	import doctest
	doctest.testmod()

#5.digit number
def num_digits(n):
	"""
	  >>> num_digits(12345)
	  5
	  >>> num_digits(0)
	  1
	  >>> num_digits(-12345)
	  5
	  >>> num_digits(-24)
	  2
	"""
	count=1
	n=abs(n)
	while n/10!=0:
		count+=1
		n/=10
	return count
if __name__ == '__main__':
	import doctest
	doctest.testmod()

#6.even digit number
def num_even_digits(n):
	"""
	  >>> num_even_digits(123456)
	  3
	  >>> num_even_digits(2468)
	  4
	  >>> num_even_digits(1357)
	  0
	  >>> num_even_digits(2)
	  1
	  >>> num_even_digits(20)
	  2
	"""
	count=0
	while n!=0:
		if n%2==0:
			count+=1
		n/=10
	return count
if __name__ == '__main__':
	import doctest
	doctest.testmod()

#7.print digit
def print_digits(n):
	"""
	  >>> print_digits(13789)
	  9 8 7 3 1
	  >>> print_digits(39874613)
	  3 1 6 4 7 8 9 3
	  >>> print_digits(213141)
	  1 4 1 3 1 2
	"""
	while n!=0:
		print n%10,
		n/=10
if __name__ == '__main__':
	import doctest
	doctest.testmod()

#8.sum of squares of digits
def sum_of_squares_of_digits(n):
	"""
	  >>> sum_of_squares_of_digits(1)
	  1
	  >>> sum_of_squares_of_digits(9)
	  81
	  >>> sum_of_squares_of_digits(11)
	  2
	  >>> sum_of_squares_of_digits(121)
	  6
	  >>> sum_of_squares_of_digits(987)
	  194
	"""
	i=0
	while n!=0:
		i+=(n%10)**2
		n/=10
	return i
if __name__ == '__main__':
	import doctest
	doctest.testmod()
