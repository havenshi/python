#~ #Example1:ball
#~ from gasp import *
#~ 
#~ begin_graphics(800, 600, title="Catch", background=color.YELLOW)
#~ set_speed(20)
#~ 
#~ ball_x = 10
#~ ball_y = 300
#~ ball = Circle((ball_x, ball_y), 10, filled=True)
#~ dx = 4
#~ dy = random_between(-4, 4)
#~ 
#~ while ball_x < 810:
	#~ if ball_y >= 590 or ball_y <= 10:
		#~ dy *= -1
	#~ ball_x += dx
	#~ ball_y += dy
	#~ move_to(ball, (ball_x, ball_y))
	#~ update_when('next_tick')
#~ 
#~ end_graphics()
#~ 
#~ #Example2:guess
#~ from gasp import *
#~ 
#~ number = random_between(1, 1000)
#~ guesses = 0
#~ 
#~ while True:
	#~ guess = input("Guess the number between 1 and 1000: ")
	#~ guesses += 1
	#~ if guess > number:
		#~ print "Too high!"
	#~ elif guess < number:
		#~ print "Too low!"
	#~ else:
		#~ print "\n\nCongratulations, you got it in %d guesses!\n\n" % guesses
		#~ break
		#~ 
#~ #Example3:respond to keyboard
#~ from gasp import *
#~ 
#~ begin_graphics(800, 600, title="Catch", background=color.YELLOW)
#~ 
#~ 
#~ mitt_x = 780
#~ mitt_y = 300
#~ mitt = Circle((mitt_x, mitt_y), 20)
#~ 
#~ while True:
	#~ if key_pressed('k') and mitt_y <= 575:
		#~ mitt_y += 5
	#~ elif key_pressed('j') and mitt_y >= 25:
		#~ mitt_y -= 5
#~ 
	#~ if key_pressed('escape'):
		#~ break
#~ 
	#~ move_to(mitt, (mitt_x, mitt_y))
	#~ update_when('next_tick')
#~ 
#~ end_graphics()
#~ 
#~ #Example4:collision
#~ from gasp import *
#~ 
#~ def distance(x1, y1, x2, y2):
	#~ return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
#~ 
#~ begin_graphics(800, 600, title="Catch", background=color.YELLOW)
#~ set_speed(20)
#~ 
#~ ball1_x = 10
#~ ball1_y = 300
#~ ball1 = Circle((ball1_x, ball1_y), 10, filled=True)
#~ ball1_dx = 4
#~ 
#~ ball2_x = 790
#~ ball2_y = 300
#~ ball2 = Circle((ball2_x, ball2_y), 10)
#~ ball2_dx = -4
#~ 
#~ while ball1_x < 790:
	#~ ball1_x += ball1_dx
	#~ ball2_x += ball2_dx
	#~ move_to(ball1, (ball1_x, ball1_y))
	#~ move_to(ball2, (ball2_x, ball2_y))
	#~ if distance(ball1_x, ball1_y, ball2_x, ball2_y) <= 20:
		#~ remove_from_screen(ball1)
		#~ remove_from_screen(ball2)
		#~ break
	#~ update_when('next_tick')
#~ 
#~ sleep(1)
#~ end_graphics()
#~ 
#~ #Example5:put pieces together
#~ from gasp import *
#~ 
#~ def distance(x1, y1, x2, y2):
	#~ return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
#~ 
#~ begin_graphics(800, 600, title="Catch", background=color.YELLOW)
#~ set_speed(120)
#~ 
#~ ball_x = 10
#~ ball_y = 300
#~ ball = Circle((ball_x, ball_y), 10, filled=True)
#~ dx = 4
#~ dy = random_between(-4, 4)
#~ 
#~ mitt_x = 780
#~ mitt_y = 300
#~ mitt = Circle((mitt_x, mitt_y), 20)
#~ 
#~ while True:
	#~ # move the ball
	#~ if ball_y >= 590 or ball_y <= 10:
		#~ dy *= -1
	#~ ball_x += dx
	#~ if ball_x > 810:       # the ball has gone off the screen
		#~ Text("Computer Wins!", (340, 290), size=32)
		#~ sleep(2)	
		#~ break
	#~ ball_y += dy
	#~ move_to(ball, (ball_x, ball_y))
#~ 
	#~ # check on the mitt
	#~ if key_pressed('k') and mitt_y <= 580:
		#~ mitt_y += 5
	#~ elif key_pressed('j') and mitt_y >= 20:
		#~ mitt_y -= 5
#~ 
	#~ if key_pressed('escape'):
		#~ break
#~ 
	#~ move_to(mitt, (mitt_x, mitt_y))
#~ 
	#~ if distance(ball_x, ball_y, mitt_x, mitt_y) <= 30:  # ball is caught
		#~ remove_from_screen(ball)
		#~ break
#~ 
	#~ update_when('next_tick')
#~ 
#~ end_graphics()
#~ 
#~ #Example6:display text
#~ from gasp import *
#~ 
#~ begin_graphics(800, 600, title="Catch", background=color.YELLOW)
#~ set_speed(120)
#~ 
#~ player_score = 0
#~ comp_score = 0
#~ 
#~ player = Text("Player: %d Points" % player_score, (10, 570), size=24)
#~ computer = Text("Computer: %d Points" % comp_score, (640, 570), size=24)
#~ 
#~ while player_score < 5 and comp_score < 5:
	#~ sleep(1)
	#~ winner = random_between(0, 1)
	#~ if winner:
		#~ player_score += 1
		#~ remove_from_screen(player)
		#~ player = Text("Player: %d Points" % player_score, (10, 570), size=24)
	#~ else:
		#~ comp_score += 1
		#~ remove_from_screen(computer)
		#~ computer = Text("Computer: %d Points" % comp_score, (640, 570), size=24)
#~ 
#~ if player_score == 5:
	#~ Text("Player Wins!", (340, 290), size=32)
#~ else:
	#~ Text("Computer Wins!", (340, 290), size=32)
#~ 
#~ sleep(4)
#~ 
#~ end_graphics()

#~ #Example7:abstraction
#~ from gasp import *
#~ 
#~ COMPUTER_WINS = 1
#~ PLAYER_WINS = 0
#~ QUIT = -1
#~ 
#~ 
#~ def distance(x1, y1, x2, y2):
	#~ return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
#~ 
#~ 
#~ def play_round():
	#~ ball_x = 10
	#~ ball_y = random_between(20, 280)
	#~ ball = Circle((ball_x, ball_y), 10, filled=True)
	#~ dx = 4
	#~ dy = random_between(-5, 5)
#~ 
	#~ mitt_x = 780
	#~ mitt_y = random_between(20, 280)
	#~ mitt = Circle((mitt_x, mitt_y), 20)
#~ 
	#~ while True:
		#~ if ball_y >= 590 or ball_y <= 10:
			#~ dy *= -1
		#~ ball_x += dx
		#~ ball_y += dy
		#~ if ball_x >= 810:
			#~ remove_from_screen(ball)
			#~ remove_from_screen(mitt)
			#~ return COMPUTER_WINS
		#~ move_to(ball, (ball_x, ball_y))
#~ 
		#~ if key_pressed('j') and mitt_y <= 580:
			#~ mitt_y += 5
		#~ elif key_pressed('k') and mitt_y >= 20:
			#~ mitt_y -= 5
#~ 
		#~ if key_pressed('escape'):
			#~ return QUIT
#~ 
		#~ move_to(mitt, (mitt_x, mitt_y))
#~ 
		#~ if distance(ball_x, ball_y, mitt_x, mitt_y) <= 30:
			#~ remove_from_screen(ball)
			#~ remove_from_screen(mitt)
			#~ return PLAYER_WINS
#~ 
		#~ update_when('next_tick')
#~ 
#~ 
#~ def play_game():
	#~ player_score = 0
	#~ comp_score = 0
#~ 
	#~ while True:
		#~ pmsg = Text("Player: %d Points" % player_score, (10, 570), size=24)
		#~ cmsg = Text("Computer: %d Points" % comp_score, (640, 570), size=24)
		#~ sleep(3)
		#~ remove_from_screen(pmsg)
		#~ remove_from_screen(cmsg)
#~ 
		#~ result = play_round()
#~ 
		#~ if result == PLAYER_WINS:
			#~ player_score += 1
		#~ elif result == COMPUTER_WINS:
			#~ comp_score += 1
		#~ else:
			#~ return QUIT
#~ 
		#~ if player_score == 5:
			#~ return PLAYER_WINS
		#~ elif comp_score == 5:
			#~ return COMPUTER_WINS
#~ 
#~ 
#~ begin_graphics(800, 600, title="Catch", background=color.YELLOW)
#~ set_speed(20)
#~ 
#~ result = play_game()
#~ 
#~ if result == PLAYER_WINS:
	#~ Text("Player Wins!", (340, 290), size=32)
#~ elif result == COMPUTER_WINS:
	#~ Text("Computer Wins!", (340, 290), size=32)
#~ 
#~ sleep(4)
#~ 
#~ end_graphics()

#1.pong
from gasp import *

COMPUTER_WINS = 1
PLAYER_WINS = 0
QUIT = -1

def hit(bx, by, r, px, py, h):
	"""
	  >>> hit(760, 100, 10, 780, 100, 100)
	  False
	  >>> hit(770, 100, 10, 780, 100, 100)
	  True
	  >>> hit(770, 200, 10, 780, 100, 100)
	  True
	  >>> hit(770, 210, 10, 780, 100, 100)
	  False
	"""
	if bx<px and px - bx <= 10 and py <= by <= (py + h):
		return True
	elif bx>px and bx - px <= 10+r and py <= by <= (py + h):
		return True
	else:
		return False
if __name__ == '__main__':
	import doctest
	doctest.testmod()
	

def play_round():
	ball_x = 400
	ball_y = 300
	ball = Circle((ball_x, ball_y), 10, filled=True)
	dx = 4
	dy = random_between(-5, 5)

	mitt_x = 780
	mitt_y = random_between(20, 280)
	r=20
	h=100
	mitt = Box((mitt_x, mitt_y), r,h)

	mitt1_x = 20
	mitt1_y = random_between(20, 280)
	r1=20
	h1=100
	mitt1 = Box((mitt1_x, mitt1_y), r1,h1)

	while True:
		ball_x += dx
		ball_y += dy
		move_to(ball, (ball_x, ball_y))
		
		if key_pressed('j') and mitt_y <= 580:
			mitt_y += 5
		elif key_pressed('k') and mitt_y >= 20:
			mitt_y -= 5

		if key_pressed('a') and mitt1_y <= 580:
			mitt1_y += 5
		elif key_pressed('s') and mitt1_y >= 20:
			mitt1_y -= 5

		if key_pressed('q'):
			return QUIT

		move_to(mitt, (mitt_x, mitt_y))
		move_to(mitt1, (mitt1_x, mitt1_y))
		
		if ball_y >= 590 or ball_y <= 10:
			dy *= -1
			
		if hit(ball_x, ball_y, r, mitt_x, mitt_y, h):
			dx *= -1

		if hit(ball_x, ball_y, r1, mitt1_x, mitt1_y, h1):
			dx *= -1

		if ball_x >= 810:
			remove_from_screen(ball)
			remove_from_screen(mitt)
			remove_from_screen(mitt1)
			return COMPUTER_WINS

		if  ball_x < 10:
			remove_from_screen(ball)
			remove_from_screen(mitt)
			remove_from_screen(mitt1)
			return PLAYER_WINS

		update_when('next_tick')


def play_game():
	player_score = 0
	comp_score = 0

	while True:
		pmsg = Text("Player: %d Points" % player_score, (10, 570), size=24)
		cmsg = Text("Computer: %d Points" % comp_score, (640, 570), size=24)
		sleep(3)
		remove_from_screen(pmsg)
		remove_from_screen(cmsg)

		result = play_round()

		if result == PLAYER_WINS:
			player_score += 1
		elif result == COMPUTER_WINS:
			comp_score += 1
		else:
			return QUIT

		if player_score == 5:
			return PLAYER_WINS
		elif comp_score == 5:
			return COMPUTER_WINS


begin_graphics(800, 600, title="Catch", background=color.YELLOW)
set_speed(60)

result = play_game()

if result == PLAYER_WINS:
	Text("Player Wins!", (340, 290), size=32)
elif result == COMPUTER_WINS:
	Text("Computer Wins!", (340, 290), size=32)

sleep(4)

end_graphics()
