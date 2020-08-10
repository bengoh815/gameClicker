import turtle
from random import randrange

# Screen
wn=turtle.Screen()
wn.setup(width=800,height=400)
wn.title("Head Clicker")
wn.bgcolor("black")
wn.tracer(0)

# Target
target=turtle.Turtle()
target.color("red")
target.shape("circle")
target.penup()
targetcoordsx=0
targetcoordsy=0

# Target movement
def hit(x,y):
    global targetcoordsx, targetcoordsy
    if withincircle(140, targetcoordsx, targetcoordsy, x, y):
        targetcoordsx=randrange(-390, 390)
        targetcoordsy=randrange(-190, 190)
        target.goto(targetcoordsx, targetcoordsy)

# Check hit
def withincircle(radius, circlex, circley, pointx, pointy):
    return (((pointx-circlex)**2+(pointy-circley)**2)<=radius)

# Keyboard binding
wn.listen()
wn.onclick(hit)



while True:
    wn.update()