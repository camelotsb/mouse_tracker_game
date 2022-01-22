import turtle #sir, i have a doubt in line 127,128
import os
import random
import time
import math

#setting up the game window

wn=turtle.Screen()
wn.bgcolor(0,0,0)
wn.title("mouse_tracker")
wn.colormode(255)
tracker1=turtle.Turtle()
tracker1.speed(0)
tracker1.hideturtle()
tracker1.setpos(350,-350)
tc=(152,146,241)
tracker1.pencolor(tc)
tracker1.seth(90)
for i in range(0,4):
    tracker1.fd(700)
    tracker1.lt(90)
tracker1.pencolor((255,255,255))
tracker1.hideturtle()
tracker1.penup()
tracker1.home()
tracker1.pendown()
tracker1.pensize(2)
tracker2=turtle.Turtle()
tracker2.color(0,0,0)
tracker2.pensize(4)
tracker1.speed(9)
tracker2.speed(9)
tracker2.pencolor("black")
tracker2.hideturtle()
#target
target=turtle.Turtle()
target.speed(0)
target.shape("circle")
target.color("red")
target.shapesize(outline=2)
target.penup()
targeth=target.clone()
gamen=1

#game starting animation 
target.pendown()
nstart=30
while nstart>0:
    x1=random.randint(-350,350)
    y1=random.randint(-350,350)
    target.setpos(x1,y1)
    targeth.setpos(target.pos())
    tracker1.setpos(target.pos())
    tracker2.setpos(tracker1.pos())
    nstart=nstart-1
else:
    gamen=0
    target.home()
    targeth.setpos(target.pos())
    tracker1.setpos(target.pos())
    tracker2.setpos(tracker1.pos())
target.penup()
wn.clearscreen()

wn=turtle.Screen()
wn.bgcolor(0,0,0)
wn.title("mouse_tracker")
wn.colormode(255)

#target
target=turtle.Turtle()
target.speed(0)
target.shape("circle")
target.color("red")
target.shapesize(outline=2)
target.penup()
targeth=target.clone()
targeth.hideturtle()
gamen=1

tracker1=turtle.Turtle()
tracker1.speed(0)
tracker1.hideturtle()
tracker1.setpos(350,-350)
tc=(152,146,241)
tracker1.pencolor(tc)
tracker1.seth(90)
for i in range(0,4):
    tracker1.fd(700)
    tracker1.lt(90)
tracker1.pencolor((255,255,255))
tracker1.hideturtle()
tracker1.penup()
tracker1.home()
tracker1.pendown()
tracker1.pensize(2)
tracker2=turtle.Turtle()
tracker2.color(0,0,0)
tracker2.pensize(4)
tracker1.speed(8)
tracker2.speed(6)
tracker2.pencolor("black")
tracker2.hideturtle()

#defining functions
def follow():
    x1,y1=target.xcor(),target.ycor()
    targeth.setpos(x1,y1)
    tracker1.setpos(x1,y1)
    tracker2.setpos(tracker1.pos())
def on_left_click(x,y):
    global score
    x1=target.xcor()
    y1=target.ycor()
    xd=(x-x1)**2
    yd=(y-y1)**2
    xyd=(xd+yd)**(1/2)
    if xyd<=10:
        ddd.color("green")
        x1=random.randint(-350,350)
        y1=random.randint(-350,350)
        target.setpos(x1,y1)
        follow()
        ddd.color("white")
        score=int((20-xyd)*10)
        ssc="score:"+str(score)
        score_board.write(ssc,font=('sans',25,'italic'))
    else:
        ddd.color("red")
        xd,yd=ddd.xcor(),ddd.ycor()
        ddd.home()
        ddd.setpos(xd,yd)
        ddd.color("white")
#listen
turtle.listen()
wn.onscreenclick(on_left_click)

t=0
score=0
score_board=turtle.Turtle()
score_board.penup()
score_board.setpos(400,350)
score_board.color("white")
score_board.pencolor("white")
#score_board.shape("arrow")
score_board.shapesize(5)
score_board.pensize(5)


ddd=turtle.Turtle()
ddd.penup()
ddd.speed(0)
ddd.setpos(0,-360)
ddd.speed(0)
ddd.shape("square")
ddd.color("white")
dddsx,dddsy=10,10
while True:
    dddx=ddd.xcor()
    dddy=ddd.ycor()
    dddx+=dddsx
    dddy+=0
    if (dddx>=-300 and dddx<=300) :
        ddd.setpos(dddx,dddy)
    else:
        dddsx=dddsx*-1
    
    
    


turtle.mainloop()



