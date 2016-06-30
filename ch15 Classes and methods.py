# Example1: convert function to method
class Time:
	def print_time(time):
		print (str(time.hours) + ":" +
			   str(time.minutes) + ":" +
			   str(time.seconds))

	def increment(self, seconds):
		self.seconds = seconds + self.seconds

		while self.seconds >= 60:
			self.seconds = self.seconds - 60
			self.minutes = self.minutes + 1

		while self.minutes >= 60:
			self.minutes = self.minutes - 60
			self.hours = self.hours + 1

	def after(self, time2):
		if self.hours > time2.hours:
			return True
		if self.hours < time2.hours:
			return False

		if self.minutes > time2.minutes:
			return True
		if self.minutes < time2.minutes:
			return False

		if self.seconds > time2.seconds:
			return True
		return False

			
current_time = Time()
current_time.hours = 9
current_time.minutes = 14
current_time.seconds = 30

current_time.print_time()       # 9:14:30

current_time.increment(500)
current_time.print_time()       # 9:22:50

done_time = Time()
done_time.hours = 12
done_time.minutes = 49
done_time.seconds = 30

		
if done_time.after(current_time):
	print "The bread will be done after it starts."


# Example2: optional arguments
def find(str, ch, start=0):
	index = start
	while index < len(str):
		if str[index] == ch:
			return index
		index = index + 1
	return -1
	
# Example3: initialization method
class Time:
	def __init__(self, hours=0, minutes=0, seconds=0):    # the attribute self.hours and the parameter hours
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds

current_time = Time(9, 14, 30)


# Example4: operator overloading
class Point:                                              # __init__ makes it easier to instantiate objects, and __str__ is useful for debugging
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __str__(self):                                    # override default built-in str function
		return '(' + str(self.x) + ', ' + str(self.y) + ')'

	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)
	
	
	def __mul__(self, other):
		return self.x * other.x + self.y * other.y
	
	def __rmul__(self, other):
		return Point(other * self.x,  other * self.y)
		
	def reverse(self):
		self.x , self.y = self.y, self.x
		
p1 = Point(3, 4)
print str(p1)                      # (3, 4)
p2 = Point(5, 7)
p3 = p1 + p2                       # p1.__add__(p2)
print p3                           # (8, 11)

print p1 * p2                      # p1.__mul__(p2), 43
print 2 * p2                       # 2.__rmul__(p2), (10, 14)
# print p2 * 2                     # p2.__mul__(2), AttributeError: 'int' object has no attribute 'x'


# Example5: polymorphism           # can take parameters with different types
def front_and_back(front):
	import copy
	back = copy.copy(front)
	back.reverse()
	print str(front) + str(back)

myList = [1, 2, 3, 4]
print front_and_back(myList)       # [1, 2, 3, 4][4, 3, 2, 1]


p = Point(3, 4)
print front_and_back(p)            # (3, 4)(4, 3) all operations in the method include copy, reverse, and print can be applied to other type Point


# 1.find
def find(str, ch, start=0, end = "None"):
    index = start
    if end == "None":
        end = len(str)
    while index < end:
        if str[index] == ch:
            return index
        index = index + 1
    return -1
