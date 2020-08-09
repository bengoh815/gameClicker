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

# Target movement
def hit(x,y):
    print(x,y)
    target.goto(randrange(-390, 390), randrange(-190, 190))

# Keyboard binding
wn.listen()
wn.onclick(hit)



while True:
    wn.update()