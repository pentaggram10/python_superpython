import turtle as t
def 원그리기(반지름,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(반지름)
    t.penup()
def 네모그리기(한변,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.forward(한변)
    t.right(90)
    t.forward(한변)
    t.right(90)
    t.forward(한변)
    t.right(90)
    t.forward(한변)
    t.penup()
def 세팅():
    t.bgcolor("wheat")
    t.shape("turtle")
    t.pensize(3)
    t.color("skyblue","skyblue")
    t.speed(0)
def 색변경(x,y):
    t.color("black","red")
    t.shape("turtle")
def 색변경2(x,y):
    t.color("skyblue","skyblue")
    t.shape("circle")
def 위():
    t.forward(30)
def 아래():
    t.backward(30)
def 오():
    t.right(90)
def 왼():
    t.left(90)
세팅()
# 원그리기(30,-230,150)
# 원그리기(50,-110,150)
# 원그리기(80,50,150)
# 네모그리기(30,150,-170)
# 네모그리기(50,50,-200)
# 네모그리기(80,-50,-200)
t.onscreenclick(t.goto)
t.ondrag(t.goto)
t.onclick(색변경)
t.onrelease(색변경2)
t.onkey(위,"Up")
t.onkey(아래,"Down")
t.onkey(오,"Right")
t.onkey(왼,"Left")

t.listen()
t.mainloop()