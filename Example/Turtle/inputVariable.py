# -*- coding: utf-8 -*-
import turtle
t = turtle.Turtle()
t.shape('turtle')
angle = int(input('회전 각도를 입력하세요>> '))
length = int(input('전진 길이를 입력하세요>> '))
t.forward(length)
for i in range (0,4):
  t.left(angle)
  t.forward(length)

turtle.exitonclick() # turtle 창이 클릭시 꺼짐