#1.wrap code
def compare(x,y):
	if x<y:
		print x,'is less than',y
	elif x>y:
		print x,'is greater than',y
	else:
		print x,'is equal to',y

compare(1,3)
compare(4,2)
compare(5,5)

#2.Boolean expression
#~ expression = raw_input("Enter a boolean expression in two variables, p and q: ")
#~ def truth_table(expression):
	#~ print " p      q      %s"  % expression
	#~ print len( " p      q      %s"  % expression)*"="
	#~ for p in True, False:
		#~ for q in True, False:
			#~ print "%-7s %-7s %-7s" % (p, q, eval(expression))
#~ truth_table(expression)
#not(p or q), not(p) and not(q) are logically equivalent;
#not(p and q), not(p) or not(q) are logically equivalent.

#3.True or False
print (True and False)
print (not(False) and True)
print (True or 7)
print (False or 7)
print (True and 0)
print (False or 8)
print ("happy" and "sad")
print ("happy" or "sad")
print ("" and "sad")
print ("happy" and "")

#4.four functions
def function_a():
    print "function_a was called A."
def function_b():
    print "function_a was called B."
def function_c():
    print "function_a was called C."
def dispatch(choice):
	if choice == 'a':
		function_a()
	elif choice == 'b':
		function_b()
	elif choice == 'c':
		function_c()
	else:
		print "Invalid choice."
dispatch('b')

#5.divisible by 3
def is_divisible_by_3(n):
	if n%3==0:
		print "This number is divisible by three."
	else:
		print "This number is not divisible by three."
is_divisible_by_3(7)
is_divisible_by_3(6)

#6.whether the first is divisible by the second
def is_divisible_by_n(x,n):
	if x%n==0:
		print "Yes, %s is divisible by %s." % (x,n)
	else:
		print "Yes, %s is not divisible by %s." % (x,n)
is_divisible_by_n(6,2)
is_divisible_by_n(5,2)

#7.test
if "Ni!":
    print 'We are the Knights who say, "Ni!"'
else:
    print "Stop it! No more of this!"

if 0:
    print "And now for something completely different..."
else:
    print "What's all this, then?"

#8.house
from gasp import *          # import everything from the gasp library

def draw_house(x,y):
	begin_graphics()            # open the graphics canvas
	Box((x, y), 100, 100)     # the house
	Box((x+35, y), 30, 50)       # the door
	Box((x+20, y+60), 20, 20)       # the left window
	Box((x+60, y+60), 20, 20)       # the right window
	Line((x, y+100), (x+50, y+140))  # the left roof
	Line((x+50, y+140), (x+100, y+100)) # the right roof

	update_when('key_pressed')  # keep the canvas open until a key is pressed
	end_graphics()              # close the canvas (which would happen
                            # anyway, since the script ends here, but it
                            # is better to be explicit).
draw_house(20,20)
