from turtle import*
import time

t=Turtle()
t.shape("triangle")
t.up()
t.speed(0)
t.goto(0,-600)




def up():
    y=t.ycor()
    y+=25
    t.goto(y,t.ycor())

def right():
    t.setheading(0)
    t.forward(25)

def left():
    t.setheading(180)
    t.forward(25)

listen()
onkey(right,"Right")
onkey(left,"Left")
onkey(up,"Up")

x=0

while True:
    if t.ycor()>-500:
        x+=0.001
        print(x)
        time.sleep(0.001)
        if t.ycor()>600:
            break
    

