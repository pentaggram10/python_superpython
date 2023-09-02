import turtle as t
import random
t.shape("square")
t.speed(0)
t.bgcolor("black")
t.pensize(7)
# def move():
#     r=random.random()
#     g=random.random()
#     b=random.random()
#     t.color(r,g,b)
    
#     t.left(10)
#     t.forward(25) 
#     t.ontimer(move,10)
def allClear():
    t.clear()
def allClear2(x,y):
    t.clear()
def randMove():
    t.penup()
    r=random.random()
    g=random.random()
    b=random.random()
    t.color(r,g,b)
    x=random.randint(-800,800)
    y=random.randint(-600,600)
    t.goto(x,y)
    t.ontimer(randMove,100)
    t.stamp()
t.ontimer(randMove,50)
t.onkey(allClear,"c")
t.onscreenclick(allClear2,3)
t.listen()
t.mainloop()