# Q3 exam mark
def grade(mark):
	if mark >= 90:
		return "A"
	else:
		if mark >= 80:
			return "B"
		else:
			if mark >= 70:
				return "C"
			else:
				if mark >= 60:
					return "D"
				else:
					return "F"

mark = 83
print( "Mark:" + str(mark), "Grade:"+ grade(mark))


# Q5 turtle bar chart 
import turtle

def drawBar(t, height):
	""" Get turtle t to draw one bar, of height. """
	t.begin_fill()               # start filling this shape
	if height < 0:
		t.write(str(height))
	t.left(90)
	t.forward(height)
	if height >= 0:
		t.write(str(height))
	t.right(90)
	t.forward(40)
	t.right(90)
	t.forward(height)
	t.left(90)
	t.end_fill()                 # stop filling this shape



xs = [48, -50, 200, 240, 160, 260, 220]  # here is the data
maxheight = max(xs)
minheight = min(xs)
numbars = len(xs)
border = 10

tess = turtle.Turtle()           # create tess and set some attributes
tess.color("blue")
tess.fillcolor("red")
tess.pensize(3)

wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")
if minheight > 0:
	lly = 0
else:
	lly = minheight - border

wn.setworldcoordinates(0-border, lly, 40*numbars+border, maxheight+border)


for a in xs:
	drawBar(tess, a)

wn.exitonclick()


# Q10 triangle is right-angled
def is_rightangled(a, b, c):
	L = sorted([a,b,c])

	result = (L[0]**2 + L[1]**2)**0.5
	if abs(result - c) < 0.001:
		return True
	else:
		return False

print is_rightangled(3,4,5)


# Q12 leap year
def leapYear(year):
    if year % 400 == 0:
        print("It's a leap year")
    elif year % 4 == 0 and not year % 100 == 0:
        print("It's a leap year")
    else:
        print("It's not a leap year")
        
print leapYear(1900)


# Q13 Easter
year = int(input("Please enter a year"))
if year >= 1900 and year <= 2099:
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19*a + 24) % 30
    e = (2*b + 4*c + 6*d + 5) % 7
    dateofeaster = 22 + d + e

    if year == 1954 or year == 2981 or year == 2049 or year == 2076:
        dateofeaster = dateofeaster - 7

    if dateofeaster > 31:
        print("April", dateofeaster - 31)
    else:
        print("March", dateofeaster)
else:
    print("ERROR...year out of range")
