import turtle

turt=turtle.screensize(600,300,'light blue')
side = int(input("Enter number of sides: "))
sideLength = int(input("Enter length of the sides: "))
circle = 360
angle = circle/side

myt = turtle.Turtle()
myt = turtle.Screen()
myt = turtle.pencolor("red")

for i in range(side): 
  myt = turtle.forward(sideLength)
  myt = turtle.left(angle)

myt = turtle.exitonclick()
