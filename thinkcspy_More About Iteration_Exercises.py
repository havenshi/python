# Q3 prime
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(25))
print(is_prime(7))


# Q5 two turtles
import random
import turtle

def moveRandom(wn, t):
    coin = random.randrange(0,2)
    if coin == 0:
        t.left(90)
    else:
        t.right(90)

    t.forward(50)

def areColliding(t1, t2):
    if t1.distance(t2) < 2:
        return True
    else:
        return False

def isInScreen(w, t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False
    return stillIn

t1 = turtle.Turtle()
t2 = turtle.Turtle()
wn = turtle.Screen()

t1.shape('turtle')
t2.shape('circle')

leftBound = -wn.window_width() / 2
rightBound = wn.window_width() / 2
topBound = wn.window_height() / 2
bottomBound = -wn.window_height() / 2

t1.up()
t1.goto(random.randrange(leftBound, rightBound),
        random.randrange(bottomBound, topBound))
t1.setheading(random.randrange(0, 360))
t1.down()

t2.up()
t2.goto(random.randrange(leftBound, rightBound),
        random.randrange(bottomBound, topBound))
t2.setheading(random.randrange(0, 360))
t2.down()


while isInScreen(wn, t1) and isInScreen(wn, t2):
    moveRandom(wn, t1)
    moveRandom(wn, t2)

wn.exitonclick()


# Q7 remove red
import image

img = image.Image("luther.jpg")
newimg = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin()

for col in range(img.getWidth()):
    for row in range(img.getHeight()):
        p = img.getPixel(col, row)

        newred = 0
        green = p.getGreen()
        blue = p.getBlue()

        newpixel = image.Pixel(newred, green, blue)

        newimg.setPixel(col, row, newpixel)

newimg.draw(win)
win.exitonclick()


# Q9 convert an image to black and white
import image

def convertBlackWhite(input_image):
    grayscale_image = image.EmptyImage(input_image.getWidth(), input_image.getHeight())

    for col in range(input_image.getWidth()):
        for row in range(input_image.getHeight()):
            p = input_image.getPixel(col, row)

            red = p.getRed()
            green = p.getGreen()
            blue = p.getBlue()

            avg = (red + green + blue) / 3.0

            newpixel = image.Pixel(avg, avg, avg)
            grayscale_image.setPixel(col, row, newpixel)

    blackwhite_image = image.EmptyImage(input_image.getWidth(), input_image.getHeight())
    for col in range(input_image.getWidth()):
        for row in range(input_image.getHeight()):
            p = grayscale_image.getPixel(col, row)
            red = p.getRed()
            if red > 140:
                val = 255
            else:
                val = 0

            newpixel = image.Pixel(val, val, val)
            blackwhite_image.setPixel(col, row, newpixel)
    return blackwhite_image


# Q11 double the size
import image

def double(oldimage):
    oldw = oldimage.getWidth()
    oldh = oldimage.getHeight()

    newim = image.EmptyImage(oldw * 2, oldh * 2)
    for row in range(oldh):
        for col in range(oldw):
            oldpixel = oldimage.getPixel(col, row)

            newim.setPixel(2*col, 2*row, oldpixel)
            newim.setPixel(2*col+1, 2*row, oldpixel)
            newim.setPixel(2*col, 2*row+1, oldpixel)
            newim.setPixel(2*col+1, 2*row+1, oldpixel)

    return newim

win = image.ImageWin()
img = image.Image("luther.jpg")

bigimg = double(img)
bigimg.draw(win)

win.exitonclick()


# Q13 pixel mapping function
import image

def pixelMapper(oldimage, rgbFunction):
    width = oldimage.getWidth()
    height = oldimage.getHeight()
    newim = image.EmptyImage(width, height)

    for row in range(height):
        for col in range(width):
            originalpixel = oldimage.getPixel(col, row)
            newpixel = rgbFunction(originalpixel)
            newim.setPixel(col, row, newpixel)

    return newim

def graypixel(oldpixel):
    intensitysum = oldpixel.getRed() + oldpixel.getGreen() + oldpixel.getBlue()
    aveRGB = intensitysum // 3
    newPixel = image.Pixel(aveRGB, aveRGB, aveRGB)
    return newPixel

win = image.ImageWin()
img = image.Image("luther.jpg")

newim = pixelMapper(img, graypixel)
newim.draw(win)

win.exitonclick()


# Q15 Sobel edge detection
import image
import math
import sys

# Code adapted from http://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/image-processing/edge_detection.html
# Licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License.

# this algorithm takes some time for larger images - this increases the amount of time
# the program is allowed to run before it times out
sys.setExecutionLimit(20000)

img = image.Image("luther.jpg")
newimg = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin()

for x in range(1, img.getWidth()-1):  # ignore the edge pixels for simplicity (1 to width-1)
    for y in range(1, img.getHeight()-1): # ignore edge pixels for simplicity (1 to height-1)

        # initialise Gx to 0 and Gy to 0 for every pixel
        Gx = 0
        Gy = 0

        # top left pixel
        p = img.getPixel(x-1, y-1)
        r = p.getRed()
        g = p.getGreen()
        b = p.getBlue()

        # intensity ranges from 0 to 765 (255 * 3)
        intensity = r + g + b

        # accumulate the value into Gx, and Gy
        Gx += -intensity
        Gy += -intensity

        # remaining left column
        p = img.getPixel(x-1, y)
        r = p.getRed()
        g = p.getGreen()
        b = p.getBlue()

        Gx += -2 * (r + g + b)

        p = img.getPixel(x-1, y+1)
        r = p.getRed()
        g = p.getGreen()
        b = p.getBlue()

        Gx += -(r + g + b)
        Gy += (r + g + b)

        # middle pixels
        p = img.getPixel(x, y-1)
        r = p.getRed()
        g = p.getGreen()
        b = p.getBlue()

        Gy += -2 * (r + g + b)

        p = img.getPixel(x, y+1)
        r = p.getRed()
        g = p.getGreen()
        b = p.getBlue()

        Gy += 2 * (r + g + b)

        # right column
        p = img.getPixel(x+1, y-1)
        r = p.getRed()
        g = p.getGreen()
        b = p.getBlue()

        Gx += (r + g + b)
        Gy += -(r + g + b)

        p = img.getPixel(x+1, y)
        r = p.getRed()
        g = p.getGreen()
        b = p.getBlue()

        Gx += 2 * (r + g + b)

        p = img.getPixel(x+1, y+1)
        r = p.getRed()
        g = p.getGreen()
        b = p.getBlue()

        Gx += (r + g + b)
        Gy += (r + g + b)

        # calculate the length of the gradient (Pythagorean theorem)
        length = math.sqrt((Gx * Gx) + (Gy * Gy))

        # normalise the length of gradient to the range 0 to 255
        length = length / 4328 * 255

        length = int(length)

        # draw the length in the edge image
        newpixel = image.Pixel(length, length, length)
        newimg.setPixel(x, y, newpixel)

newimg.draw(win)
win.exitonclick()
