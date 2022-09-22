import turtle #1. import modules
import random
import pygame
import math

pygame.init()
window = pygame.display.set_mode()

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
michelangelo.pd()
leonardo.pd()
for i in range(11):
  mDistance = random.randrange(1,11)
  michelangelo.forward(mDistance)
  lDistance = random.randrange(1,11)
  leonardo.forward(lDistance)
  


# PART B - complete part B here
pygame.draw.polygon(window,'red',)
cords=[]
num_sides=
side_length=
offset=


window.exitonclick()
