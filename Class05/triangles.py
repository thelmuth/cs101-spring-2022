import math
from turtle import *
colormode(255)

april = Turtle()

april.speed(1)
april.width(3)

# side = 129
side = int(input("What should the length of the first side be? "))
hypotenuse = math.sqrt(side ** 2 + side * side)

### To fill in a drawn shape:
april.fillcolor("darkorchid")
april.begin_fill()

april.forward(side)
april.left(90)

april.forward(side)
april.left(180 - 45)
# april.left(45)

april.forward(hypotenuse)

april.end_fill()


### Draw second triangle

april.up()
april.goto(-200, 100) # move turtle to a specific location
april.down()
april.setheading(0)


side1 = 78

# side1 = side1 + 100

hypotenuse = 2 * side1

side2 = math.sqrt(hypotenuse * hypotenuse - side1 * side1)

april.fillcolor("limegreen")
april.begin_fill()

april.forward(side2)
april.right(180 - 30)
april.forward(hypotenuse)
april.right(180 - 60)
april.forward(side1)

april.end_fill()

### print allows us to show text or numbers to the user
### Ex:
print(hypotenuse)
print("The length of side2 is", side2)






