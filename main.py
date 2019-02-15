#!/bin/python3

from turtle import *
from random import randint

speed(1000)
penup()
goto(-140,140)

for step in range(15):
  write(step, align='center')
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)

ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()
ada.left(360)

josh = Turtle()
josh.color('blue')
josh.shape('turtle')

josh.penup()
josh.goto(-160,70)
josh.pendown()
josh.left(360)

bob = Turtle()
bob.color('green')
bob.shape('turtle')

bob.penup()
bob.goto(-160,40)
bob.pendown()
bob.right(360)

betty = Turtle()
betty.color('orange')
betty.shape('turtle')

betty.penup()
betty.goto(-160, 10)
betty.pendown()
betty.right(360)

for turn in range(100):
  ada.forward(randint(1,5))
  josh.forward(randint(1,5))
  bob.forward(randint(1,5))
  betty.forward(randint(1,5))
