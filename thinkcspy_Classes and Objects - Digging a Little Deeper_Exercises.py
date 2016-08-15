class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)


class Rectangle:
    """Rectangle class using Point, width and height"""

    def __init__(self, initP, initW, initH):

        self.location = initP
        self.width = initW
        self.height = initH

    def area(self):
        return self.width * self.height
        
    def transpose(self):
        temp = self.width
        self.width = self.height
        self.height = temp

    def diagonal(self):

        d = (self.width**2 + self.height**2) ** 0.5
        return d
                
loc = Point(4, 5)
r = Rectangle(loc, 6, 5)
print(r)



