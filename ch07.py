#Example
import string
def is_lower(ch):
	return string.find(string.lowercase, ch) != -1
print(is_lower('a'))
def is_lower1(ch):
	return ch in string.lowercase
print(is_lower1('B'))
def is_lower2(ch):
	return 'a' <= ch <= 'z'
print(is_lower2('c'))

#1.test
fruit='rambutan'
print(type(fruit))  #<type 'str'>
print(len(fruit))   #8
print(fruit[:3])    #'ram'

group = "John, Paul, George, and Ringo"
print(group[12:18])   #'George'
print(group[6:10])    #'Paul'
print(group[:4])      #'John'
print(group[24:])     #'Ringo'

s='Janeones'
print(len(s))         #8
print(s[4:6])=='on'   #True

#1.modify
prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
	if letter=='O' or letter=='Q':
		print letter +'u'+ suffix
	else:
		print letter+suffix

#2.encapsulate
def count_letters(letter,ch):
	count = 0
	for char in letter:
		if char == ch:
			count += 1
	print count
count_letters('banana','a')

def count_letters1(letter,ch):
	count = 0
	for i in range(len(letter)):
		if string.find(letter,ch,i,i+1)!=-1:
			count += 1
	print count
count_letters1('bananana','a')

#3.reverse
def reverse(s):
	"""
	  >>> reverse('happy')
	  'yppah'
	  >>> reverse('Python')
	  'nohtyP'
	  >>> reverse("")
	  ''
	  >>> reverse("P")
	  'P'
	"""
	char=''
	i=len(s)-1
	while i >= 0:
		char+=s[i]
		i-=1
	return char
if __name__ == '__main__':
	import doctest
	doctest.testmod()

#4.mirror
def forward(s):
	char=''
	i=0
	while i <= len(s)-1:
		char+=s[i]
		i+=1
	return char
def mirror(s):
	"""
	  >>> mirror("good")
	  'gooddoog'
	  >>> mirror("yes")
	  'yessey'
	  >>> mirror('Python')
	  'PythonnohtyP'
	  >>> mirror("")
	  ''
	  >>> mirror("a")
	  'aa'
	"""
	return forward(s)+reverse(s)
if __name__ == '__main__':
	import doctest
	doctest.testmod()

#5.remove
def remove_letter(letter, strng):
	"""
	  >>> remove_letter('a', 'apple')
	  'pple'
	  >>> remove_letter('a', 'banana')
	  'bnn'
	  >>> remove_letter('z', 'banana')
	  'banana'
	  >>> remove_letter('i', 'Mississippi')
	  'Msssspp'
	"""
	s=''
	i=0
	while i<len(strng):
		if letter!=strng[i]:
			s+=strng[i]
		i+=1
	return s
if __name__ == '__main__':
	import doctest
	doctest.testmod()

#6.lots of functions
def is_palindrome(s):
	"""
	  >>> is_palindrome('abba')
	  True
	  >>> is_palindrome('abab')
	  False
	  >>> is_palindrome('tenet')
	  True
	  >>> is_palindrome('banana')
	  False
	  >>> is_palindrome('straw warts')
	  True
	"""
	if len(s)%2==0:
		i=0
		while i<=(len(s)/2-1):
			if s[i]!=s[len(s)-1-i]:
				return False
			i+=1
		return True
	else:
		j=0
		while j<=(len(s)-1)/2-1:
			if s[j]!=s[len(s)-1-j]:
				return False
			j+=1
		return True
if __name__ == '__main__':
	import doctest
	doctest.testmod()
	

def remove(sub, s):
	"""
	  >>> remove('an', 'banana')
	  'bana'
	  >>> remove('cyc', 'bicycle')
	  'bile'
	  >>> remove('iss', 'Mississippi')
	  'Missippi'
	  >>> remove('egg', 'bicycle')
	  'bicycle'
	"""
	if string.find(s,sub)!=-1:
		re=string.find(s,sub)
		s=s[:re]+s[re+len(sub):]
		return s
	return s
if __name__ == '__main__':
	import doctest
	doctest.testmod()
	
	
def remove_all(sub, s):
	"""
	  >>> remove_all('an', 'banana')
	  'ba'
	  >>> remove_all('cyc', 'bicycle')
	  'bile'
	  >>> remove_all('iss', 'Mississippi')
	  'Mippi'
	  >>> remove_all('eggs', 'bicycle')
	  'bicycle'
	"""
	while string.find(s,sub)!=-1:
		re=string.find(s,sub)
		s=s[:re]+s[re+len(sub):]
	return s
if __name__ == '__main__':
	import doctest
	doctest.testmod()
	
		
#7.fix
# -*- coding: utf-8 -*-
print '%s %d %f' % (5, 5, 5)
print '%-.2f' % 3
print '%-10.2f%-10.2f' % (7, 1.0/2)
print '$%5.2fn $%5.2fn $%5.2f' % (3, 4.5, 11.2)
print '%s %s %s' % ('this', 'that', 'something')
print '%s %s %s %s' % ('yes', 'no', 'up', 'down')
print '%d %f %s' % (3, 3, 'three')




