from turtle import *
colormode(255)


larry = Turtle()
larry.width(5)

turtle_color = input("What color do you want the star to be? ")
larry.color(turtle_color)

### If you want the user to enter RGB colors
# r = int(input("Enter R: "))
# g = int(input("Enter G: "))
# b = int(input("Enter B: "))
# 
# larry.color(r, g, b)


for _ in range(8):
    ## Code here will run every time through the loop
    larry.forward(200)
    larry.right(90 + 45)
    
# Unindented code will not be repeated
# Only run after the loop above has run 8 times
larry.color("gray")
larry.up()
larry.backward(200)
larry.down()

for _ in range(5):
    larry.forward(150)
    larry.right(90 + 54)

larry.color("green")
larry.up()
larry.backward(200)
larry.down()

## Draws a rectangle
for _ in range(2):
    larry.forward(100)
    larry.right(90)
    larry.forward(200)
    larry.right(90)
    
    
