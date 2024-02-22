#CS175

#Lucas Vandenakker 

#Turtle Graphics Stop Sign
import math
import turtle

# Named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -20

# Size the window.
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)


# Calculate the diameter of the octagon so we
# can center it in the graphics window.
#                s
#        ---------------
#       / |             \
#  s   /  |              \
#     /   | x             \  s
#    /    |                \
#   |------                 |
#   |   x                   |
#   |                       |
#   To get the diameter:
#     diameter = s + 2 * x
#   We know that s is 100.
#   Use Pythagoras to get x:
#   s^2 = x^2 + x^2
#   s^2 = 2*x^2
#   x = s / sqrt(2)
s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)

radius = diameter / 2
# Initialize the turtle.


turtle.speed(ANIMATION_SPEED)


turtle.width(10)
turtle.color('red')
# Move the turtle to the starting point.
turtle.penup()
turtle.backward(radius)
turtle.left(90)
turtle.forward(radius/2)
turtle.pendown()


# Draw the octagon.

for i in range(NUM_SIDES):
   turtle.right(ANGLE)
   turtle.forward(LENGTH)


turtle.penup()
turtle.goto(0,0)
turtle.right(90)
turtle.backward(radius-20)
turtle.left(90)
turtle.forward((radius-20)/2)
turtle.pendown()
turtle.fillcolor("red")
turtle.begin_fill()
for i in range(NUM_SIDES):
    turtle.right(ANGLE)
    turtle.forward(83)

turtle.end_fill()  


# Display 'STOP'
turtle.color('white')
turtle.penup()
turtle.goto(TEXT_X, TEXT_Y)
turtle.write("STOP", align = 'center',font=("Arial",35, "bold"))
