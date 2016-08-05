# Q3 loop
for amonth in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'November', 'December']:
    print("One of the months of the year is %s" % amonth)


# Q4 list
for i in [12, 10, 32, 3, 66, 17, 42, 99, 20]:
	print i
	
for i in [12, 10, 32, 3, 66, 17, 42, 99, 20]:
	print i**2


# Q5 turtle
# triangle
import turtle

wn = turtle.Screen()
triangle = turtle.Turtle()

for i in range(3):
    triangle.forward(100)
    triangle.left(120)

wn.exitonclick()

# square
import turtle

wn = turtle.Screen()
square = turtle.Turtle()

for i in range(4):
    square.forward(100)
    square.left(90)

wn.exitonclick()

# hexagon
import turtle

wn = turtle.Screen()
hexagon = turtle.Turtle()

for i in range(6):
    hexagon.forward(100)
    hexagon.left(60)

wn.exitonclick()

# octagon
import turtle

wn = turtle.Screen()
octagon = turtle.Turtle()

for i in range(8):
    octagon.forward(100)
    octagon.left(45)

wn.exitonclick()


# Q6 fill polygon
sides = int(input("the number of sides:"))
angle = 360 / sides 
length = int(input("the length of the side:"))
line_color = input("the color of lines:")
fill_color = input("the color of polygon:")

import turtle
wn = turtle.Screen()
tess = turtle.Turtle()

tess.color(line_color)    
tess.fillcolor(fill_color)    
tess.begin_fill()    
for i in range(sides):    
        tess.forward(length)   
        tess.left(angle)    
tess.end_fill()

wn.exitonclick()


# Q7 drunk
import turtle

wn = turtle.Screen()
drunk = turtle.Turtle()

# move the turtle forward a little so that the whole path fits on the screen
drunk.penup()
drunk.forward(60)

drunk.pendown()
for angle in [160, -43, 270, -97, -43, 200, -940, 17, -86]:

    # positive angles are counter-clockwise and negative angles are clockwise
    drunk.left(angle)
    drunk.forward(100)

# the .heading() method gives us the turtle's current heading in degrees
print("The pirate's final heading was", drunk.heading())

wn.exitonclick()


# Q9 five star
import turtle

turing = turtle.Turtle()

for i in range(5):
    turing.forward(100)
    turing.left(216)


# Q10 turtle
import turtle

wn=turtle.Screen()
wn.bgcolor("lightgreen")

t=turtle.Turtle()      # turtle
t.shape("turtle")
t.color("blue")
t.stamp()              # circle turtle
move=30

for i in range(12):
	t.penup()          # Pull the pen up -- not drawing when moving.
	t.forward(50)
	t.pendown()        # Pull the pen down -- drawing when moving.
	t.forward(25)
	t.penup()
	t.forward(15)
	t.stamp()
	t.home()
	t.right(move)
	move+=30
	
wn.exitonclick()


# Q13 spider
import turtle

wn = turtle.Screen()

babbage = turtle.Turtle()
babbage.shape("triangle")

n = int(input("How many legs should this sprite have? "))
angle = 360 / n

for i in range(n):
    # draw the leg
    babbage.right(angle)
    babbage.forward(65)
    babbage.stamp()

    # go back to the middle and turn back around
    babbage.right(180)
    babbage.forward(65)
    babbage.right(180)

babbage.shape("circle")
