import turtle,math


screen=turtle.Screen()
screen.bgcolor("black")
screen.setup(750,750)
t=turtle.Turtle()
t.speed(0)


def rectangle(width,lengh):
    for i in range(2):
        t.forward(lengh)
        t.left(90)
        t.forward(width)
        t.left(90)  
def trapeze(down,up):
    c=((down-up)/2)*math.sqrt(2)
    t.forward(down)
    t.left(135)
    t.forward(c)
    t.left(45)
    t.forward(up)
    t.left(45)
    t.forward(c)
def ellipse(rad):
    for i in range(2):
        t.circle(rad,90)
        t.circle(rad//2,90)
def hexagon(width):
    for i in range(6):
        t.forward(width)
        t.left(360/6)
def rhombus(width):
    for i in range(2):
        for j in range(2):
            t.left(60)
            t.forward(width)
        t.left(60)


t.color("red")
rhombus(100)
turtle.done()