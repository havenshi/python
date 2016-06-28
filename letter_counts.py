import sys

lower_str =sys.argv[1].lower()

letter_counts = {}
for letter in lower_str:
   if 97<=ord(letter)<=122:     # letter.isalpha()
	   letter_counts[letter] = letter_counts.get(letter, 0) + 1

letter_items = letter_counts.items()
letter_items.sort()

for item in letter_items:
	print '%-3s%d' % (item[0],item[1])


# $ python letter_counts.py "ThiS is String with Upper and lower case Letters."
