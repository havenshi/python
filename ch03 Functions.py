#1.print 25 lines
def three_lines():
	print
	print
	print
	
def nine_lines():
	three_lines()
	three_lines()
	three_lines()

def clear_screen():
	nine_lines()
	nine_lines()
	three_lines()
	three_lines()
	print

clear_screen()

#2.cat n times
def cat_n_times(s,n):
	print s*n

cat_n_times('Spam',7)

#test input and raw_input
a=input()
print a    #'a'>a, 1>1, h>error

b=raw_input()
print a    #'a'>'a', 1>1, h>h

