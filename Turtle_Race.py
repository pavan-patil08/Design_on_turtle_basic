import turtle
from random import *
from turtle import *

penup()
goto(-140,140) #positioning the pen

for sp in range(15): #loop for creating the lines labelled with numbers
    speed(10)
    #setting the speed
    write(sp)
    #writing the int
    right(90)
    #setting right at 90 degrees
    forward(10)
    #forward at 10 units
    pendown()
    #ready to draw
    forward(150)
    #forward at 150 units
    penup()
    #not ready to draw
    backward(160)
    #back at 160 units
    left(90)
    #left set at 90 degrees
    forward(20)
    #forward at 20 units

pavan = Turtle() #inheriting the turtle
pavan.color('green') #setting the color to green for the first turtle
pavan.shape('turtle') #setting the shape to "turtle"
pavan.penup() #not ready to draw
pavan.goto(-160, 100) #positioning the turtle
pavan.pendown()  #ready to draw

patil = Turtle() #inheriting the turtle
patil.color('red') #setting the color to red for the second turtle
patil.shape('turtle') #setting the shape of the "turtle"
patil.goto(-160, 80) #positioning
patil.pendown() #ready to draw

turtleVar = Turtle() #inheriting the last turtle
turtleVar.color('blue') #setting the color to blue for the last turtle
turtleVar.shape('turtle') #setting the shape of the "turtle"
turtleVar.goto(-160, 60) #positioning
turtleVar.pendown() #ready

for turn in range(100): #loop for race 
    pavan.forward(randint(1,5)) #setting the speed randomly with the "random" module
    patil.forward(randint(1,5)) #setting the speed randomly with the "random" module
    turtleVar.forward(randint(1,5)) #setting the speed randomly with the "random" module

turtle.done()