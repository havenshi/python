# Q1 
import turtle

def draw_continue_Square(t, sz):
	"""Make turtle t draw a square of with side sz."""
	for i in range(4):
		t.forward(sz)
		t.left(90)

wn = turtle.Screen()       # Set up the window and its attributes
wn.bgcolor("lightgreen")

alex = turtle.Turtle()     # create alex
alex.color('hotpink')
alex.pensize(3)

for i in range(5):
	draw_continue_Square(alex, 20)   # Call the function to draw the square
	alex.penup()
	alex.forward(40)       # move alex to the starting position for the next square
	alex.pendown()

wn.exitonclick()


# Q2
import turtle

def jump(t, l):     # move to lower-left corner
	t.penup()
	t.backward(l)
	t.right(90)
	t.forward(l)
	t.left(90)
	t.pendown()
	
def draw_contain_Square(t, sz):
	"""Make turtle t draw a square of with side sz."""
	for i in range(4):
		t.forward(sz)
		t.left(90)
	jump(t, 10)

wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()           # create tess and set some attributes
tess.color("hotpink")
tess.pensize(3)

for i in range(5):
	draw_contain_Square(tess, 20 * (i + 1))

wn.exitonclick()


# Q3 
import turtle

def drawPoly(t, num_sides, side_length):
	for i in range(num_sides):
		t.forward(side_length)
		t.left(360/num_sides)

wn = turtle.Screen()       # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color('hotpink')
tess.pensize(3)

drawPoly(tess, 8, 50)

wn.exitonclick()


# Q4
import turtle

def rotate(t,num):
	t.left(360/num)

def draw_central_Square(t, num):
	for i in range(4):
		t.forward(100)
		t.left(90)
	rotate(t,num)

wn = turtle.Screen()       # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color('blue')
tess.pensize(2)

for i in range(20):
	draw_central_Square(tess, 20)

wn.exitonclick()


# Q5
import turtle

def drawSpiral(t, angle):
	''' takes a turtle, t, and an angle in degrees '''
	length = 1
	for i in range(84):
		t.forward(length)
		t.right(angle)
		length = length + 2


wn = turtle.Screen()       # Set up the window and its attributes
wn.bgcolor("lightgreen")

guido = turtle.Turtle()    # create guido
guido.color('blue')

## draw the first spiral ##
# position guido
guido.penup()
guido.backward(110)
guido.pendown()

# draw the spiral using a 90 degree turn angle
drawSpiral(guido, 90)


## draw the second spiral ##
# position guido
guido.home()
guido.penup()
guido.forward(90)
guido.pendown()

drawSpiral(guido, 89)

wn.exitonclick()

# Q7 sum of all integer numbers
def sumTo(n):
	return (n * (n + 1)) / 2
	
print sumTo(10)


# Q8 area of a circle of radius r
def areaOfCircle(r) :
	return 3.14*r**2

print areaOfCircle(2)


# Q10
import turtle

def drawFivePointStar(t):
	for i in range(5):
		t.forward(100)
		t.left(216)
	t.penup()
	t.forward(350)
	t.right(144)
	t.pendown()

wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()           # create tess and set some attributes
tess.color("hotpink")
tess.pensize(3)

for i in range(5):
	drawFivePointStar(tess)

wn.exitonclick()


# Q11
import turtle

def drawStar(t, n):
	for i in range(n):
		t.forward(100)
		t.left(180 - 180/n)

stroustrup = turtle.Turtle()
drawStar(stroustrup, 7)

wn.exitonclick()


# Q14 square root of a number
def mySqrt(n):
	oldguess = n * 0.5
	newguess = 0.5 * (oldguess + (n/oldguess))
	
	while newguess != oldguess:
		oldguess = newguess
		newguess = 0.5 * (oldguess + (n/oldguess))
			
	return newguess

print mySqrt(2)


# Q15 pi
def myPi(iters):
    ''' Calculate an approximation of PI using the Leibniz
    approximation with iters number of iterations '''
    pi = 0
    sign = 1
    denominator = 1
    for i in range(iters):
        pi = pi + (sign/denominator)
        sign = sign * -1  # alternate positive and negative
        denominator = denominator + 2

    pi = pi * 4.0
    return pi

pi_approx = myPi(10000)
print(pi_approx)


# Q17 sprite
import turtle

def drawSprite(t, numlegs, leglength):
   angle = 360/numlegs
   for i in range(numlegs):
      t.forward(leglength)
      t.backward(leglength)
      t.left(angle)

def drawFancySquare(t, sz, lgs, lgl):
   for i in range(4):
       t.forward(sz)
       drawSprite(t, lgs, lgl)
       t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
drawFancySquare(alex, 100, 10, 15)

wn.exitonclick()
