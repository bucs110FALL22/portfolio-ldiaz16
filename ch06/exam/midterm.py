import turtle
import random

turt = turtle.Screen()
turt = turtle.setup(width=510, height=500)
turt = turtle.Turtle()
turt = turtle.color('black')


def main():
    x = 0
    reset()
    cityType = input("Enter city type [major or minor]: ")
  # setting odds
    for i in range(10):
        if (cityType == "major"):
            x = random.randint(1, 4)
            if x == 4:
                building_with_spire(cityType)
            else:
                building(cityType)
        elif (cityType == "minor"):
            x = random.randint(1, 6)
            if x == 6:
                building_with_spire(cityType)
            else:
                building(cityType)
        space(cityType)


#if major city is chosen, buildings have 25% chance at spire, if minor city spires have 16% chance of being generated


def building(city):
  width = building_width(city)
  height = building_height(city)
  turt = turtle.left(90)
  turt = turtle.forward(height)
  turt = turtle.right(90)
  turt = turtle.forward(width)
  turt = turtle.right(90)
  turt = turtle.forward(height)
  turtle.left(90)


def building_with_spire(city):
  height = building_height(city)
  turt = turtle.left(90)
  turt = turtle.forward(height)
  turt = turtle.right(30)
  turt = turtle.forward(50)
  turt = turtle.right(120)
  turt = turtle.forward(50)
  turt = turtle.right(30)
  turt = turtle.forward(height)
  turt = turtle.left(90)


#random height generator based on type of city
def building_height(type):
    randY = 0
    if type == "major":
        randY = random.randint(130, 220)
    elif type == "minor":
        randY = random.randint(100, 170)
    return randY

#minor cities have "fatter" buildings while major cities have 'skinnier ones'
def building_width(type):
  randX = 0
  if type == 'major':
    randX = random.randint(40,50)
  if type == 'minor':
    randX = random.randint(45,65)
  return randX

#if major city is chosen, spaces are from 3-6 units wide, while if its a minor city spaces will be 7-10 units wide
def space(city):
    space = 0
    if city == "minor":
        space = random.randint(7, 10)
    elif city == "major":
        space = random.randint(3, 6)
    turt = turtle.forward(space)


def reset():
    turtle.penup()
    turtle.left(180)
    turtle.forward(248)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.pendown()
    street()

#creates street design
def street():
    turt = turtle.pensize(50)
    turt = turtle.forward(590)
    turt = turtle.right(180)
    turt = turtle.forward(590)
    turt = turtle.right(180)
    turt = turtle.pensize(5)
    turt = turtle.color('yellow')
    for i in range(12):
        turt = turtle.forward(30)
        turt = turtle.penup()
        turt = turtle.forward(20)
        turt = turtle.pendown()
    turt = turtle.penup()
    turt = turtle.left(180)
    turt = turtle.forward(600)
    turt = turtle.right(90)
    turt = turtle.forward(20)
    turt = turtle.right(90)
    turt = turtle.pensize(2)
    turt = turtle.color('black')
    turt = turtle.pendown()


main()
turt = turtle.exitonclick()
