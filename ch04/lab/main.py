import pygame
import random
import math

pygame.init()
RED = (255,0,0)
WHITE = (255, 255, 255)


size = [600,274]
screen = pygame.display.set_mode(size)

screen.fill(WHITE)
width, height = pygame.display.get_window_size()
print(width)
width = 274
#draw.circle requires center point of surface, which can be found by dividing both x and y sizes by 2, this goes for the radius aswell

centerOf = (width/2,height/2)
radiusOf = (width/2)

radiusOf2 = (width/2)
centerOf2 = (width+radiusOf2,height/2)

pygame.draw.circle(screen,RED,(centerOf),(radiusOf))
pygame.draw.circle(screen,'purple',(centerOf2),(radiusOf2))

#red circle
pygame.draw.line(screen,'black',[0,radiusOf],[274,radiusOf],3)
pygame.draw.line(screen,'black',[radiusOf,0],[radiusOf,274],3)

#purple circle
pygame.draw.line(screen,'black',[width,radiusOf],[548,radiusOf],3)
pygame.draw.line(screen,'black',[width+radiusOf,0],[radiusOf+width,274],3)

#part B and c
for i in range(10):
  x = random.randrange(0,width)
  y = random.randrange(0,height)
  distance_from_center = math.hypot(radiusOf-x, radiusOf-y)
  is_in_circle = distance_from_center <= radiusOf
  if is_in_circle == True:
    pygame.draw.circle(screen,'blue',[x,y],3)
  else:
    pygame.draw.circle(screen,'orange',[x,y],3)
  pygame.time.wait(800)
  pygame.display.flip()
  x2 = random.randrange(width,width*2)
  y2 = random.randrange(0,height)
  distance_from_center = math.hypot((width+radiusOf2)-x2,(radiusOf-y2))
  is_in_circle = distance_from_center <= radiusOf
  if is_in_circle == True:
    pygame.draw.circle(screen,'yellow',[x2,y2],3)
  else:
    pygame.draw.circle(screen,'green',[x2,y2],3)
  pygame.time.wait(800)
  pygame.display.flip()
  




#player1 is blue and orange
#player2 is yellow and green
pygame.display.flip()
pygame.time.wait(7001)
#submitting