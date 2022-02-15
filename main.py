import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here

# Race 1
michelangelo.forward(random.randrange(1, 101))
leonardo.forward(random.randrange(1, 101))

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# Race 2
for i in range(10):
  michelangelo.forward(random.randrange(0, 11))
  leonardo.forward(random.randrange(0, 11))

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# Part B - complete part B here
sides = [4, 6, 9, 12]
length = 30

for i in sides:
  turn_angle = 360/i
  michelangelo.pendown()
  for j in range(i):
    michelangelo.forward(length)
    michelangelo.left(turn_angle)
  michelangelo.clear()

window.exitonclick()
