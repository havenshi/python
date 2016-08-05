import turtle            # set up alex
wn = turtle.Screen()
alex = turtle.Turtle()

for aColor in ["yellow", "red", "purple", "blue"]:
   alex.color(aColor)
   alex.forward(50)
   alex.left(90)

wn.exitonclick()
