import turtle

sides = int(input("Enter number of sides: "))
sideLength = int(input("Enter length of the sides: "))
circle = 360
angle = circle/sides

myt = turtle.Turtle()
myt = turtle.Screen()
myt = turtle.pencolor("red")

for i in range(sides): 
  myt = turtle.forward(sideLength)
  myt = turtle.left(angle)

myt = turtle.exitonclick()
