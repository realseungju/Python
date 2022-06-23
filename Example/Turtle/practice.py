import turtle
t = turtle.Turtle()
t.shape('turtle')
t.forward(200)
for i in range(0,2):
  t.right(90)
  t.forward(10)
  t.right(90)
  t.forward(200)
  t.left(90)
  t.forward(10)
  t.left(90)
  t.forward(200)
t.right(90)
t.forward(200)
t.circle(50)

turtle.exitonclick()