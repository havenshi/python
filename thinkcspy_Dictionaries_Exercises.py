x = input("Enter a sentence:")

x = x.lower()   # convert to all lowercase

alphabet = 'abcdefghijklmnopqrstuvwxyz'

letter_count = {} # empty dictionary
for char in x:
    if char in alphabet: # ignore any punctuation, numbers, etc
        if char in letter_count:
            letter_count[char] = letter_count[char] + 1
        else:
            letter_count[char] = 1

keys = letter_count.keys()
keys.sort()
for char in keys:
    print(char, letter_count[char])





d = {'apples': 15, 'bananas': 35, 'grapes': 12}

d['oranges'] = 20
print len(d)

print 'grapes' in d

d.get('pears', 0)

fruits = d.keys()
fruits.sort()
print(fruits)

del d['apples']
print 'apples' in d




#~ f = open('alice.txt', 'r')
#~ 
#~ count = {}
#~ 
#~ for line in f:
    #~ for word in line.split():
#~ 
        #~ # remove punctuation
        #~ word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
        #~ word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
        #~ word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
        #~ word = word.replace(']', '').replace(';', '')
#~ 
        #~ # ignore case
        #~ word = word.lower()
#~ 
        #~ # ignore numbers
        #~ if word.isalpha():
            #~ if word in count:
                #~ count[word] = count[word] + 1
            #~ else:
                #~ count[word] = 1
#~ 
#~ keys = count.keys()
#~ keys.sort()
#~ 
#~ # save the word count analysis to a file
#~ out = open('alice_words.txt', 'w')
#~ 
#~ for word in keys:
    #~ out.write(word + " " + str(count[word]))
    #~ out.write('\n')
#~ 
#~ print("The word 'alice' appears " + str(count['alice']) + " times in the book.")




pirate = {}
pirate['sir'] = 'matey'
pirate['hotel'] = 'fleabag inn'
pirate['student'] = 'swabbie'
pirate['boy'] = 'matey'
pirate['restaurant'] = 'galley'
# and so on

sentence = input("Please enter a sentence in English")

psentence = []
words = sentence.split()
for aword in words:
    if aword in pirate:
        psentence.append(pirate[aword])
    else:
        psentence.append(aword)

print(" ".join(psentence))
