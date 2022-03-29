import turtle
t = turtle.Turtle()
t.shape('turtle')

angle = 120
length = 100

for i in range (0,3):
  t.right(angle)
  t.forward(length)


turtle.exitonclick() # turtle window will close when you click.