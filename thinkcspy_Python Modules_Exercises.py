# Q1 print 10 random numbers
import random

for i in range(10):
	arandom = random.random()
	print(arandom)


# Q2 print 10 random numbers between 25 and 35
import random

for i in range(10):
	arandom = random.randrange(25,35)
	print(arandom)


# Q3 right triangle 
import math

side1 = 3
side2 = 4
hypotenuse = math.hypot(side1,side2)
print(hypotenuse)


# Q4 calculate an approximation for pi
#~ pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...
	 #~ 0     1     2     3     4     5     ...
	 
def nth_term(n):
	return 4 / (2.0 * n + 1) * (-1) ** n
	
def appr_pi(n):
	pi = 0
	for i in range(n):
		pi += nth_term(i)
	return pi

print appr_pi(1000000)
