import turtle as t
import random
score=0
def right():
    if bar.xcor()<300:
        bar.forward(50)
def left():
    if bar.xcor()>-300:
        bar.backward(50)
def randcolor():
    r=random.random()
    g=random.random()
    b=random.random()
    ball.color(r,g,b)

def restart():
    global score
    ballx=15
    bally=6
    while True:
        ball.setx(ball.xcor()+ballx)
        ball.sety(ball.ycor()+bally)
        
        if ball.xcor()>300:
            ballx*=-1
        elif ball.xcor()<-300:
            ballx*=-1
        if ball.ycor()>300:
            bally*=-1
        elif ball.ycor()<-300:
            bally*=-1
        if(bar.xcor()-50<ball.xcor()<bar.xcor()+50)and(-250<ball.ycor()<-240):
            bally*=-1
            score+=1
            board.clear()
            board.write(f"score:{score}",font=("garamond",20,"bold"))
        if(ball.ycor()<-290):
            board.clear()
            board.write(f"score:{score}",font=("garamond",20,"bold"))
            ball.goto(0,0)
            break
s=t.Screen()
s.screensize(600,600,"darkgreen")
s.onkey(right,"Right")
s.onkey(left,"Left")
ball=t.Turtle()
ball.speed(0)
ball.penup()
ball.shape("circle")
ball.goto(0,0)
ball.shapesize(2,2)
t.onkey(restart,"s")
board=t.Turtle()
board.speed(0)
board.penup()
board.hideturtle()
board.color("white")
board.goto(-55,270)
board.write(f"SCORE:{score}",font=("garamond",20,"bold"))
bar=t.Turtle()
bar.speed(0)
bar.penup()
bar.color("gold")
bar.shape("square")
bar.shapesize(1,5)
bar.goto(0,-260)
s.listen()
s.mainloop()
