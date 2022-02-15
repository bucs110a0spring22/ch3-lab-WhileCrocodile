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

if michelangelo.xcor() == leonardo.xcor():
  print("Race 1 was a tie!")
elif michelangelo.xcor() > leonardo.xcor():
  print("Michaelangelo won Race 1!")
else:
  print("Leonardo won Race 1!")

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
  
# Race 2
for i in range(10):
  michelangelo.forward(random.randrange(0, 11))
  leonardo.forward(random.randrange(0, 11))

if michelangelo.xcor() == leonardo.xcor():
  print("Race 2 was a tie!")
elif michelangelo.xcor() > leonardo.xcor():
  print("Michaelangelo won Race 2!")
else:
  print("Leonardo won Race 2!")

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# Part B - complete part B here
sides = [4, 6, 9, 12]
length = 30

michelangelo.pendown()

for sides_in_shape in sides:
  turn_angle = 360/sides_in_shape
  for number_of_turns in range(sides_in_shape):
    michelangelo.forward(length)
    michelangelo.left(turn_angle)
  michelangelo.clear()

print("Your shapes have been drawn (and cleared).")

window.exitonclick()
