import turtle,math


screen=turtle.Screen()
screen.bgcolor("black")
screen.setup(750,750)
t=turtle.Turtle()
t.speed(0)


def rectangle(width,lengh,col):
    t.begin_fill()
    t.color(col)
    for i in range(2):
        t.forward(lengh)
        t.left(90)
        t.forward(width)
        t.left(90)
    t.end_fill()
def trapeze(down,up,col):
    t.begin_fill()
    t.color(col)
    c=((down-up)/2)*math.sqrt(2)
    t.forward(down)
    t.left(135)
    t.forward(c)
    t.left(45)
    t.forward(up)
    t.left(45)
    t.forward(c)
    t.left(135)
    t.end_fill()
def ellipse(rad):
    for i in range(2):
        t.circle(rad,90)
        t.circle(rad//2,90)
def hexagon(width,col):
    t.color(col)
    t.begin_fill()
    for i in range(6):
        t.forward(width)
        t.left(360/6)
    t.end_fill()
def rhombus(width,col):
    t.begin_fill()
    t.color(col)
    for i in range(2):
        for j in range(2):
            t.left(60)
            t.forward(width)
        t.left(60)
    t.end_fill()
def name():
    t.write("Mikołaj Suchan group number:ZZISS1-1114",font=("Arial",15,"bold")) 


col=["blue","green","yellow","orange","red"]
val=10
num=0
angle=[270,180,90,0]
rangle=[0,180,270,90]
position=[160,50,-160,-50,160]
#kod właściwy


for i in range(36):
    t.seth(-val)
    t.color(col[num])
    if num==4:
        num=0
    else:
        num+=1
    ellipse(100)
    val+=10
for j in range(4):
    t.up()
    t.goto(position[j],position[j+1])
    t.down()
    t.setheading(angle[j])
    hexagon(100,col[0])
    for k in range(6):
        trapeze(100,50,col[1])
        t.forward(100)
        t.left(60)
    t.up()
    t.left(90)
    t.forward(100*math.sqrt(3))
    t.right(90)
    t.down()
    rectangle(50,100,col[2])
    t.up()
    t.left(90)
    t.forward(50)
    t.right(90)
    t.down()
    if j==0:
        t.setheading(rangle[j])
        rhombus(80,col[4])
        t.up()
        t.right(90)
        t.forward(100)
        t.down()
        t.setheading(rangle[j+1])
        rhombus(80,col[4])
    elif j==1:
        t.setheading(rangle[j+1])
        rhombus(80,col[4])
        t.up()
        t.right(90)
        t.forward(100)
        t.down()
        t.setheading(rangle[j+2])
        rhombus(80,col[4])
    elif j==2:
        t.setheading(rangle[j-1])
        rhombus(80,col[4])
        t.up()
        t.right(90)
        t.forward(100)
        t.down()
        t.setheading(rangle[j-2])
        rhombus(80,col[4])
    elif j==3:
        t.setheading(rangle[j])
        rhombus(80,col[4])
        t.up()
        t.right(90)
        t.forward(100)
        t.down()
        t.setheading(rangle[j-1])
        rhombus(80,col[4])
t.color(col[2])
t.up()
t.goto(300,300)
t.down()
name()
t.hideturtle()
turtle.done()