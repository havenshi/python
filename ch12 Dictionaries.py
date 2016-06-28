#Example1:dictionary
eng2sp = {}
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
print eng2sp

#Example2:matrix
matrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3}
print matrix.get((1, 3), 0)           #0,second argument is the value get should return if the key is not in the dictionary

#Example3:fibonacci
previous = {0: 0, 1: 1}

def fibonacci(n):
	if previous.has_key(n):
		return previous[n]
	else:
		new_value = fibonacci(n-1) + fibonacci(n-2)
		previous[n] = new_value
		return new_value
print fibonacci(100)                  #354224848179261915075L

#Example4:count
letter_counts = {}
for letter in "Mississippi":
   letter_counts[letter] = letter_counts.get (letter, 0) + 1
print letter_counts                   #{'M': 1, 's': 4, 'p': 2, 'i': 4}

letter_items = letter_counts.items()  #[(,),(,)]
letter_items.sort()                   #sort only works on list, not dict
print letter_items                    #[('M', 1), ('i', 4), ('p', 2), ('s', 4)]


#Example5:robots
#
# robots.py
#
from gasp import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GRID_WIDTH = SCREEN_WIDTH/10 - 1
GRID_HEIGHT = SCREEN_HEIGHT/10 - 1                    # grid,(63,47)


def place_player():
	x = random.randint(0, GRID_WIDTH)                 # a random integer 
	y = random.randint(0, GRID_HEIGHT)
	return {'shape': Circle((10*x+5, 10*y+5), 5, filled=True), 'x': x, 'y': y}  # player is circle. dict,{'shape','x','y'}

def place_robot(x, y, junk=False):
	return {'shape': Box((10*x, 10*y), 10, 10, filled=junk), 'x': x, 'y': y, 'junk': junk}                 # robot is box. dict,{'shape','x','y'}

def place_robots(numbots):                            # place all the robots in a list if they don't collide
	robots = []
	for i in range(numbots):            # 3.check each remaining robots to see if they have collided with another robot, disgard all the robots and place a pile of junk at the locations they occupied
		x = random.randint(0, GRID_WIDTH)
		y = random.randint(0, GRID_HEIGHT)
		robots.append(place_robot(x, y, junk=False))
	return robots

junk = []
	
def move_player(player):
	update_when('key_pressed')
	if key_pressed('escape'):
		return True                                                 # y<G
	elif key_pressed('4'):                                 #       __ __ __
		if player['x'] > 0: player['x'] -= 1               #      |        |
	elif key_pressed('7'):                                 # x>0  |        |  x<G
		if player['x'] > 0: player['x'] -= 1               #      |__ __ __|
		if player['y'] < GRID_HEIGHT: player['y'] += 1             
	elif key_pressed('8'):                                          # y>0
		if player['y'] < GRID_HEIGHT: player['y'] += 1
	elif key_pressed('9'):
		if player['x'] < GRID_WIDTH: player['x'] += 1
		if player['y'] < GRID_HEIGHT: player['y'] += 1
	elif key_pressed('6'):
		if player['x'] < GRID_WIDTH: player['x'] += 1
	elif key_pressed('3'):
		if player['x'] < GRID_WIDTH: player['x'] += 1
		if player['y'] > 0: player['y'] -= 1
	elif key_pressed('2'):
		if player['y'] > 0: player['y'] -= 1
	elif key_pressed('1'):
		if player['x'] > 0: player['x'] -= 1
		if player['y'] > 0: player['y'] -= 1
	else:
		return False

	move_to(player['shape'], (10*player['x']+5, 10*player['y']+5)) # player move,circle(10*x+5,10*y+5)

	return False

def collided(thing1, thing2):
	return thing1['x'] == thing2['x'] and thing1['y'] == thing2['y'] # game end as soon as the player is caught, or else the robot just follows her
																	 
def check_collisions(robots, junk, player):
	# check whether player has collided with anything
	for thing in robots + junk:
		if collided(thing, player):                    # 1.check whether the player has collided with a robot or a pile of junk, set defeated to true and break out of the game loop
			return "robots_win"
			
	# remove robots that have collided with a pile of junk
	for robot in reversed(robots):                     # ! if use unreversed, when first collision is detected and that robot is removed, second robot move into the first position in the list and it is missed by the next iteration
		for pile in junk:
			if collided(robot, pile):                  # 2.heck each robot in list to see if it has collided with a pile of junk, disgard the robot from list       
				robots.remove(robot)
				
	# return False                                      # returns true when the player has collided with something and lost the game, and false when the player has not lost and the game should continue


	# robots is not empty and the player has not collided with anything -- the game is still in play
	# the player has collided with something -- the robots win
	# the player has not collided with anything and robots is empty -- the player wins


	# remove robots that collide and leave a pile of junk  # 3.check each remaining robots to see if they have collided with another robot, disgard all the robots and place a pile of junk at the locations they occupied
	for index, robot1 in enumerate(robots):                # (1)check each robot in robots (outer loop, traversing forward)
		for robot2 in reversed(robots[index+1:]):          # (2)compare it with every robot that follows it (inner loop, traversing backw)
			if collided(robot1, robot2):                   # (3)mark the first robot as junk, and remove the second one
				robot1['junk'] = True
				junk.append(place_robot(robot1['x'], robot1['y'], True))
				remove_from_screen(robot2['shape'])
				robots.remove(robot2)

	for robot in reversed(robots):                         # (4)once all robots have been checked for collisions, traverse the robots list once again in reverse, removing all robots marked as junk
		if robot['junk']:
			remove_from_screen(robot['shape'])
			robots.remove(robot)
	
	if not robots:
		return "player_wins"

	return ""

def move_robot(robot, player):
	if robot['x'] < player['x']: robot['x'] += 1                   # x,y+-1,move to player
	elif robot['x'] > player['x']: robot['x'] -= 1

	if robot['y'] < player['y']: robot['y'] += 1
	elif robot['y'] > player['y']: robot['y'] -= 1

	move_to(robot['shape'], (10*robot['x'], 10*robot['y']))        # robot move,box(10*x,10*y)
	
def move_robots(robots, player):
	for robot in robots:
		move_robot(robot, player)

def play_game():
	begin_graphics(SCREEN_WIDTH, SCREEN_HEIGHT, title="Robots")
	player = place_player()
	robots = place_robots(2)
	defeated = False                                               # not defeated true
	while not defeated:                                            # event loop
		quit = move_player(player)          # press escape key causes move_player to return True, make not defeated false, break
		if quit:
			break
		move_robots(robots, player)         # move player and move robot
		defeated = check_collisions(robots, junk, player)  # false > loop, true(collide) > out loop

	if defeated:                            # check for defeated if it is true and display an appropriate message
		remove_from_screen(player['shape'])
		for thing in robots + junk:         # remove the new junk from the screen
			remove_from_screen(thing['shape'])
		Text("They got you!", (240, 240), size=32)
		sleep(3)

	end_graphics()

#~ if __name__ == '__main__':
	#~ play_game()


# 1.test
d = {'apples': 15, 'bananas': 35, 'grapes': 12}
print d['bananas']

d['oranges'] = 20
print len(d)

print d.has_key('grapes')

print d.get('pears', 0)

fruits = d.keys()
fruits.sort()
print fruits                    # ['apples', 'bananas', 'grapes', 'oranges']

del d['apples']
print d.has_key('apples')       # False

def add_fruit(inventory, fruit, quantity=0):
	"""
	Adds quantity of fruit to inventory.

	  >>> new_inventory = {}
	  >>> add_fruit(new_inventory, 'strawberries', 10)
	  >>> new_inventory.has_key('strawberries')
	  True
	  >>> new_inventory['strawberries']
	  10
	  >>> add_fruit(new_inventory, 'strawberries', 25)
	  >>> new_inventory['strawberries']
	  35
	"""
	if inventory.has_key(fruit):
		inventory[fruit] += quantity
	else:
		inventory[fruit] = quantity
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()

# 2.Alice
import string

source = open('alice_in_wonderland.txt', 'r')
text = source.read()
source.close()

newfile = open('alice_words.txt', 'w')

def count(text):
	for i in reversed(range(len(text))):                   # alpha remain
		if (not text[i].isalpha()) and text[i]!=' ':
			text=text[:i]+text[i+1:]
	
	lower_text=text.lower()                  # lower         
	
	word_list=string.split(lower_text)       # remove space, transfer to list
	
	
	word_count_dict={}                       # count every word
	for single_word in word_list:
		word_count_dict[single_word]=word_count_dict.get(single_word,0)+1
	
	counts_list = word_count_dict.items()    # [(,),(,)]
	counts_list.sort()                       # sort
	
	return counts_list
	
counts_list=count(text)                      # extract result

newfile.write('%-18s%s\n' % ('Word','Count'))
newfile.write('='*23+'\n')
for item in counts_list:
	newfile.write('%-18s%d\n' % (item[0],item[1]))


newfile.close()

#3. longest
longest=('',0)
for item in counts_list:
	if len(item[0])>longest[1]:
		longest=(item[0],len(item[0]))
print longest
