
## Need these things in order to use turtles:

from turtle import *

colormode(255) # This makes it easier to manipulate colors

# This is our turtle, stored in a variable named leo
leo = Turtle()

leo.speed(5) # slows down leo so we can see what's happening
leo.width(3) # Increases the pen's width to 3 pixels wide

# This tells leo to move forward 80 pixels
leo.forward(80)
leo.left(60)
leo.forward(110)

leo.right(150)
leo.forward(200)
leo.left(60)
leo.backward(300)

## Recall above. Let's run through this using the debugger

# pick up the pen and go somewhere else
leo.up()

leo.right(40)
leo.forward(80)
leo.down()

leo.circle(100)

leo.up()
leo.forward(200)
leo.down()

## Draw a triangle
leo.pencolor("red") # "red" is a string of text, and needs the quotes
leo.forward(100)
leo.right(120)

leo.pencolor("blue")
leo.forward(100)
leo.right(120)

leo.pencolor("magenta")
leo.forward(100)
leo.right(120)







