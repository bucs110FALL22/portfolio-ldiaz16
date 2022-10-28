import turtle #1. import modules
import random
import pygame
import math

pygame.init()
window = pygame.display.set_mode()

window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')
michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')
michelangelo.speed(6)
leonardo.speed(6)

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
 
## 5. Your PART A code goes here
michelangelo.pd()
leonardo.pd()

mRandx = random.randrange(1,101)
lRandx = random.randrange(1,101)

michelangelo.goto(mRandx,20)
leonardo.goto(lRandx,-20)

if mRandx > lRandx:
  winDiff = mRandx - lRandx
  print("Michelangelo beat Leonardo by",winDiff,"units")

elif lRandx > mRandx:
  winDiff = lRandx - mRandx
  print("Leonardo beat Michelangelo by",winDiff,"units")

else:
  print("Leonardo and Michelangelo tied")

pygame.time.wait(2000)

michelangelo.color('lightblue')
leonardo.color('lightblue')
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

mSum = 0
lSum = 0

michelangelo.color('orange')
leonardo.color('blue')
michelangelo.pd()
leonardo.pd()

for i in range(11):
  mDistance = random.randrange(1,11)
  mSum += mDistance
  michelangelo.forward(mDistance)
  lDistance = random.randrange(1,11)
  lSum += lDistance
  leonardo.forward(lDistance)
if mSum > lSum:
  winDiff = mSum - lSum
  print("Michelangelo won by",winDiff,"units")
elif lSum > mSum:
  winDiff = lSum - mSum 
  print("Leonardo won by",winDiff,"units")
else:
  print("The race was tied")
pygame.time.wait(2000)


michelangelo.color('lightblue')
leonardo.color('lightblue')
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
window.exitonclick()



# PART B - complete part B here

numShapes = int(input("Enter amount of shapes you'd like to draw: "))
coords = []

def draw_eq_shape():
  for i  in range(num_sides):
    theta = ((2.0 * math.pi * i) / num_sides)
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    coords.append([x,y])
  pygame.draw.polygon(window,'red',coords)
  pygame.display.flip()
  coords = []
  pygame.time.wait(2000)
  window = window.fill('black')
  pygame.display.flip()

for i in range(numShapes):
  window = pygame.display.set_mode()
  shapeNum = i + 1
  print("Enter number of sides of polygon",shapeNum,": ")
  num_sides = int(input(''))
  print("Enter length of the sides of polygon",shapeNum,": ")
  side_length = int(input(""))
  
  offset = side_length + 10
  for i  in range(num_sides):
    theta = ((2.0 * math.pi * i) / num_sides)
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    coords.append([x,y])
  pygame.draw.polygon(window,'red',coords)
  pygame.display.flip()
  coords = []
  pygame.time.wait(2000)
  window = window.fill('black')
  pygame.display.flip()
