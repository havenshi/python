# Example: class
class Point:                        # the first parameter self refers to the instance being created
    def __init__(self, x=0, y=0):   # initialization method, all point instances ought to have x and y attributes
        self.x = x
        self.y = y

    def distance_from_origin(self): # method
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
        
p = Point()
print type(Point)    # <type 'classobj'>
print type(p)        # <type 'instance'>

# The variable p refers to a Point object, which contains two attributes. Each attribute refers to a number.

p.x=3
p.y=4
print '(%d, %d)' % (p.x, p.y)  #(3,4)

p2 = Point()
print p2.x           # 0

p3 = Point(5, 12)
print p3.x            # 5
print p3.y            # 12
print p3.distance_from_origin()  # 13.0


# 1. hexadecimal
class Point:
	pass

p = Point()
print id(p)         # 140153380617320
print hex(id(p))    # 0x7f7800773c68
print p             # <__main__.Point instance at 0x7f7800773c68>

print hex(id(p)) in repr(p) #True
# x = 'foo', repr(x)>>"'foo'", repr gives the string containing the representation of the value 'foo' assigned to x
print repr(p)       # <__main__.Point instance at 0x7ff2b7847c68>

print repr(p).rpartition(' ')[-1][:-1] # 0x7f7800773c68  
hexadecimal_id = repr(p).rpartition(' ')[-1][:-1]  # parse out the hexadecimal string. splits on the last space, and take whatever comes after it with [-1] (last element)

print int(hexadecimal_id, 16)                      #140153380617320
print int(hexadecimal_id, 16) == id(p)             #True


# 2. distance
def distance(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    result = (dx**2 + dy**2)**0.5
    return result
