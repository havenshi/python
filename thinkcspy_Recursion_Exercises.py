# Q1
def reverseList(lst):
	#your code here
	if len(lst)==1:
		return lst
	else:
		lastone=lst.pop()
		return [lastone]+reverseList(lst)

print reverseList(['Hello',33,'!'])



# Q2
def computeFactorial(number):
	#your code here
	if number==1:
		return 1
	else:
		return number*computeFactorial(number-1)
		
print computeFactorial(8)


# Q5
def fibonacci(n):
	if n == 0 or n == 1:
		return n
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)

print fibonacci(10)


def f(n):
	a, b = 0, 1
	for i in range(0, n):
		a, b = b, a + b
	return a
print f(10)


# Q6 Tower of Hanoi
def Hanoi(num,fromh,toh,midh):
	if num==1:
		pass
	else:
		Hanoi(num-1,fromh,midh,toh)
		print('move from',fromh,'to',toh)
		Hanoi(num-1,midh,toh,fromh)
	
Hanoi(5,'A','B','C')


# Q7 Hilbert curve

