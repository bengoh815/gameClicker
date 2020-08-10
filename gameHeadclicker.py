import turtle
from random import randrange

# Screen
wn=turtle.Screen()
wn.setup(width=800,height=600)
wn.title("Head Clicker")
wn.bgcolor("black")
wn.tracer(0)

# Stats board
statsboard=turtle.Turtle()
statsboard.speed(0)
statsboard.ht()
statsboard.penup()
statsboard.color("white")
statsboard.goto(0,270)

# Target
target=turtle.Turtle()
target.speed(0)
target.color("red")
target.shape("circle")
target.penup()
targetcoordsx=0
targetcoordsy=0
targethits=0
totalhits=0

# Target movement
def hit(x,y):
    global targetcoordsx, targetcoordsy,targethits, totalhits
    totalhits+=1
    statsboard.clear()
    if withincircle(140, targetcoordsx, targetcoordsy, x, y):
        targethits+=1
        targetcoordsx=randrange(-390, 390)
        targetcoordsy=randrange(-290, 290)
        target.goto(targetcoordsx, targetcoordsy)
    # Write statsboard
    statsboard.write("Accuracy: {0:.2f}%".format((targethits/totalhits)*100),align="Center", font=("Courier", 24, "normal"))


# Check hit
def withincircle(radius, circlex, circley, pointx, pointy):
    return (((pointx-circlex)**2+(pointy-circley)**2)<=radius)

# Keyboard binding
wn.listen()
wn.onclick(hit)


while True:
    wn.update()