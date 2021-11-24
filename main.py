import turtle

t = turtle.Turtle()
t.speed(0) 
wn = turtle.Screen()
wn.bgcolor("black")

colors = ['deep sky blue', 'deep sky blue', 'deep sky blue', 'deep sky blue', 'deep sky blue', 'hot pink', 'hot pink', 'hot pink', 'hot pink', 'hot pink', 'white', 'white', 'white', 'white', 'white', 'hot pink', 'hot pink', 'hot pink', 'hot pink', 'hot pink', 'deep sky blue', 'deep sky blue', 'deep sky blue', 'deep sky blue', 'deep sky blue']
 
def nextshape(length):
  t.pu()
  t.fd(length)
  t.pd()

def nextrow():
  t.pu()
  t.bk(250)
  t.rt(90)
  t.fd(50)
  t.lt(90)
  t.pd()

def draw_square(myColor, length):
  myColor = colors.pop(0)
  t.color(myColor)
  t.begin_fill()
  for i in range(4):
    t.fd(length)
    t.lt(90)
  t.end_fill()

for j in range(5):
  for i in range(5):
    draw_square(colors, 50)
    nextshape(50)
  nextrow()