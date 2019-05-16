import turtle
t = turtle.Turtle()
t.shape('turtle')
t.screen.bgcolor('black')
t.color('white')
t.speed('fastest')

for i in range(10,200,5):
    t.circle(i)
for j in range(10,200, 5):
    t.circle(-j)
t.right(90)
for j in range(10,200, 5):
    t.circle(j,360)
t.left(180)
for j in range(10,200, 5):
    t.circle(j,360)


turtle.done()
