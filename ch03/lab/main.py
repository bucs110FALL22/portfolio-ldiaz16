import turtle #1. import modules
import random
import pygame
import math

pygame.init()
window = pygame.display.set_mode()


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
