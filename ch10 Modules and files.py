#Example1
from seqtools import remove_at   #no .py
s = "A string!"
print remove_at(4, s)

import seqtools                  #no .py
s = "A string!"
print seqtools.remove_at(4, s)

#Exmaple2
mylist=[5,27,3]

print mylist.append(12)
print mylist                     #[5,27,3,12]

print mylist.insert(1, 12)
print mylist                     #[5, 12, 27, 3, 12]

print mylist.count(12)           #2

print mylist.extend([5, 9, 5, 11])
print mylist                     #[5, 12, 27, 3, 12, 5, 9, 5, 11]

print mylist.index(9)            #6

print mylist.count(5)            #3

print mylist.reverse()
print mylist                     #[11, 5, 9, 5, 12, 3, 27, 12, 5]

print mylist.sort()
print mylist                     #[3, 5, 5, 5, 9, 11, 12, 12, 27]

print mylist.remove(12)
print mylist                     #[3, 5, 5, 5, 9, 11, 12, 27]


#Example3:textfile
myfile = open('test.dat', 'w')
print myfile

myfile.write("Now is the time")
myfile.write("to close the file")

myfile.close()

myfile = open('test.dat', 'r')
text = myfile.read()             #Now is the timeto close the file
print text
myfile = open('test.dat', 'r')   #reopen
print myfile.read(5)             #Now i
print myfile.read()              #s the timeto close the file


def copy_file(oldfile, newfile):
	infile = open(oldfile, 'r')
	outfile = open(newfile, 'w')
	while True:
		text = infile.read(50)
		if text == "":
			break
		outfile.write(text)
	infile.close()
	outfile.close()
	return

outfile = open("test.dat","w")
outfile.write("line one\nline two\nline three\n")
outfile.close()

infile = open("test.dat","r")
print infile.readline()           #line one+next newline character(empty line)
print infile.readlines()          #['line two\n', 'line three\n'] remaining
print infile.readline()           #nothing left
print infile.readlines()          #[]

def filter(oldfile, newfile):
	infile = open(oldfile, 'r')
	outfile = open(newfile, 'w')
	while True:
		text = infile.readline()
		if text == "":
		   break
		if text[0] == '#':        #omit lines begin with #
		   continue
		outfile.write(text)
	infile.close()
	outfile.close()
	return


#Example4:Alice in Wonderland
#
# countletters.py
#

def display(i):
	if i == 10: return 'LF'       #'\n'
	if i == 13: return 'CR'       #'\r'
	if i == 32: return 'SPACE'    #' '
	return chr(i)

infile = open('alice_in_wonderland.txt', 'r')
text = infile.read()
infile.close()

counts = 128 * [0]

for letter in text:
	counts[ord(letter)] += 1      #128(0~127) kinds of letters, list counts

outfile = open('alice_counts.dat', 'w')
outfile.write("%-12s%s\n" % ("Character", "Count"))
outfile.write("=================\n")

for i in range(len(counts)):
	if counts[i]:
		outfile.write("%-12s%d\n" % (display(i), counts[i]))

outfile.close()

#Example5:sys and argv
#
# demo_argv.py
#
import sys
print sys.argv                           #['ch10.py']
										 # $ python demo_argv.py this and that 1 2 3 > ['demo_argv.py', 'this', 'and', 'that', '1', '2', '3']


#
# sum.py
#
from sys import argv

nums = argv[1:]

for index, value in enumerate(nums):
	nums[index] = float(value)

print sum(nums)
										# $ python sum.py 3 4 5 11  > 23.0    argv[0] is .py itself



#1.pydoc
import calendar
year = calendar.calendar(2008)
print year   
print calendar.isleap(2008)


import math
print math.ceil(22.4)
print math.floor(-13.6)
from math import sqrt
print sqrt(2)


import copy
a = [1, 2, 3, 4, ['a', 'b']]  #origin

b = a                         #assignment
c = copy.copy(a)              #copy super object
d = copy.deepcopy(a)          #deepcopy super/sub object

a.append(5)                   #amend list
a[4].append('c')              #amend sublist

print 'a = ', a               #a =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
print 'b = ', b               #b =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
print 'c = ', c               #c =  [1, 2, 3, 4, ['a', 'b', 'c']]
print 'd = ', d               #d =  [1, 2, 3, 4, ['a', 'b']]

#2.age and name
import mymodule1
import mymodule2
print (mymodule2.myage - mymodule1.myage) == (mymodule2.year - mymodule1.year)

import mymodule1              #When import, __name__ ==mymodule1, __name__ != '__main__', not execute print. 
import mymodule2              #When import, __name__ ==mymodule2, __name__ != '__main__', not execute print. 

print "My name is %s" % __name__
if __name__ == '__main__':
	print "This won't run if I'm  imported."                #__name__ == '__main__', execute print. 

#3.function and method
class MyClass:
	def f():  
		return "hello world"  
x = MyClass()  
print x.f.__class__             #<class 'method'>  
print MyClass.f.__class__       #<class 'function'>  

import string

a=string.capitalize('maryland') #function
b='maryland'.capitalize()       #method
print a==b                       #True


def myreplace(old, new, s):
	"""
	Replace all occurences of old with new in the string s.
	  >>> myreplace(',', ';', 'this, that, and, some, other, thing')
	  'this; that; and; some; other; thing'
	  >>> myreplace(' ', '**', 'Words will now be separated by stars.')
	  'Words**will**now**be**separated**by**stars.'
	"""
	return string.join(string.split(s,old),new)        #also written as new.join(s.split(old))
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()

#4.test
def cleanword(word):
	"""
	  >>> cleanword('what?')
	  'what'
	  >>> cleanword('"now!"')
	  'now'
	  >>> cleanword('?+="word!,@$()"')
	  'word'
	"""
	clean=''
	for i in range(len(word)):
		if word[i].isalpha():
			clean+=word[i]
	return clean
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()


def has_dashdash(s):
	"""
	  >>> has_dashdash('distance--but')
	  True
	  >>> has_dashdash('several')
	  False
	  >>> has_dashdash('critters')
	  False
	  >>> has_dashdash('spoke--fancy')
	  True
	  >>> has_dashdash('yo-yo')
	  True
	"""
	return s.count('-')!=0
if __name__ == '__main__':
	import doctest
	doctest.testmod()


def extract_words(s):
	"""
	  >>> extract_words('Now is the time!  "Now", is the time? Yes, now.')
	  ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now']
	  >>> extract_words('she tried to curtsey as she spoke--fancy')
	  ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy']
	"""
	if has_dashdash(s)==True:
		s=s.replace('-',' ')
	new_list=s.split()
	list=[]
	for i in range(len(new_list)):
		char=cleanword(new_list[i]).lower()
		list+=[char]
	return list
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()


def wordcount(word, wordlist):
	"""
	  >>> wordcount('now', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
	  ['now', 2]
	  >>> wordcount('is', ['now', 'is', 'time', 'is', 'now', 'is', 'the', 'is'])
	  ['is', 4]
	  >>> wordcount('time', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
	  ['time', 1]
	  >>> wordcount('frog', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
	  ['frog', 0]
	"""
	return [word, wordlist.count(word)]

if __name__ == '__main__':
	import doctest
	doctest.testmod()


def wordset(wordlist):
	"""
	  >>> wordset(['now', 'is', 'time', 'is', 'now', 'is', 'is'])
	  ['is', 'now', 'time']
	  >>> wordset(['I', 'a', 'a', 'is', 'a', 'is', 'I', 'am'])
	  ['I', 'a', 'am', 'is']
	  >>> wordset(['or', 'a', 'am', 'is', 'are', 'be', 'but', 'am'])
	  ['a', 'am', 'are', 'be', 'but', 'is', 'or']
	"""
	for word in wordlist:
		if wordlist.count(word) > 1:
			for a in range(wordlist.count(word) - 1):
				wordlist.remove(word)
	wordlist.sort()
	return wordlist
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()


def longestword(wordset):
	"""
	  >>> longestword(['a', 'apple', 'pear', 'grape'])
	  5
	  >>> longestword(['a', 'am', 'I', 'be'])
	  2
	  >>> longestword(['this', 'that', 'supercalifragilisticexpialidocious'])
	  34
	"""
	initial=0
	for i in range(len(wordset)):
		if len(wordset[i])>initial:
			initial=len(wordset[i])
	return initial
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()


#5.sort fruit
source = open('unsorted_fruits.txt', 'r')
fruits = source.readlines()
print(type(fruits))                        #list
source.close()
fruits.sort()
newfile = open('sorted_fruits.txt', 'w')
newfile.writelines(fruits)
newfile.close()
