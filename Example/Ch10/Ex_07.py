import turtle
t = turtle.Turtle()
t.shape('turtle')
shapeAngle = [(0,0,120,120,120,45,45,45,45,45,45,45,45)]
for points in shapeAngle:
  t.up()
  t.goto(points[0],points[1])
  t.down()

  for num in range(2,5):
    t.forward(50)
    t.left(points[num])

  t.up()
  t.goto(100,0)
  t.down()

  for num in range(5,len(points)):
    t.forward(50)
    t.left(points[num])
