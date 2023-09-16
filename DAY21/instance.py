import turtle as t
class CturtleConfig:
    def __init__ (self,색="black"):
        self.객체=t.Turtle()
        self.색=색
        self.settings()
    def settings(self):
        self.객체.color(self.색)
        self.객체.shape("turtle")        
        self.객체.penup()
                
t1=CturtleConfig("gold")
t.onscreenclick(t1.객체.goto,1)
t2=CturtleConfig("navy")
t.onscreenclick(t2.객체.goto,3)
t.mainloop()