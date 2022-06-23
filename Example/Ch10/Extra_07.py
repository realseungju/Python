import turtle
t = turtle.Turtle()
t.shape('turtle')
shapeAngle = [(0,0,120,120,120),(150,0,90,90,90,90),(0,150,72,72,72,72,72),(150,150,45,45,45,45,45,45,45,45)]
for points in shapeAngle:
  t.up()
  t.goto(points[0],points[1])
  t.down()

  for num in range(2,len(points)):
    t.forward(50)
    t.left(points[num])