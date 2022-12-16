"""import turtle
t= turtle.Turtle()
t.screen.bgcolor('black')
t.pensize(2)
t.color('green')
t.left(90)
t.backward(100)
t.speed(200)
t.shape('turtle')

def tree(i):
    
    if  i<10:
       return

    else:
       t.forward(i)
       t.color('orange')
       t.circle(2)
       t.color('brown')
       t.left(30)
       tree(3*i/4)
       t.right(60)
       tree(3*i/4)
       t.left(30)
       t.backward(i)

 tree(100)
  turtle.done() """





# -*- coding: utf-8 -*-
from errno import ERANGE
import turtle
class Lindenmayer(turtle.Turtle):
    "Bracketed L System"
    syms = {
        "F":"gforward",
        "f":"jforward",
        "+":"tright",
        "-":"tleft",
        "A":"gforward",
        "B":"gforward",
        "U":"penup",
        "D":"pendown",
        "[":"push_stack",
        "]":"pop_stack",
        "1":"color1", # black by default
        "2":"color2", # red by default
        "3":"color3", # green by default
        "4":"color4", # blue by default
    }
    def draw(self):
        self.hideturtle() # to speed up the drawing
        for x in self.string:
            try:
                getattr(self,Lindenmayer.syms[x])()
            except KeyError:
                "For actions that don't do anything"
                pass
    def gforward(self): self.forward(self.d)
    def jforward(self):
        "Go forward, but don't draw"
        self.penup()
        self.forward(self.d)
        self.pendown()
    def tleft(self):
        "Turn left by degrees"
        self.left(self.a)
    def tright(self):
        "Turn right by degrees"
        self.right(self.a)
    def push_stack(self):
        "push state to stack"
        self._stack.append((self.pos(), self.heading()))
    def pop_stack(self):
        "pop and restore state"
        pos, heading = self._stack.pop()
        self.penup()
        self.setpos(pos)
        self.setheading(heading)
        self.pendown()
    def color1(self):
        self.pencolor("#000000")
    def color2(self):
        self.pencolor("#ff0000")
    def color3(self):
        self.pencolor("#00ff00")
    def color4(self):
        self.pencolor("#0000ff")
    def fix_rules(self):
        "Add unspecified conversions. They stay the same"
        parts = set("".join(self.rules.keys() + self.rules.values()))
        for x in parts:
            if not x in self.rules.keys():
                self.rules[x] = x
    def init(self, depth, speed=0):
        "Prepare required variables before draw"
        self._stack = []
        self.speed(speed)
        self.depth = depth
        string = self.begin
        self.fix_rules()
        for _ in ERANGE(depth):
            string = "".join(self.rules[x] for x in string)
        self.string = string
        self.after_init()
    def after_init(self):
        "Extra stuff, executed right after init function"
        pass
#### Begin L-System Equations 
class koch(Lindenmayer):
    rules = {'F':'F-F++F-F'}
    begin = "F"
    a = 60
    def after_init(self): self.d = max(400 / 3 ** self.depth,1) # set distance appopropiate to complexity
class square_koch(Lindenmayer):
    rules = {'F':'F-F+F+F-F'}
    begin = "F"
    a = 90
    def after_init(self): self.d = max(400 / 3 ** self.depth,1)
class sierpinsky(Lindenmayer):
    rules = {'A':'B-A-B', 'B':'A+B+A'}
    begin = 'A'
    a = 60
    def after_init(self): self.d = max( 300 / 2 ** self.depth,1)
class fibonacci_tree(Lindenmayer):
    rules = {'A':'AA', 'B': 'A[-B]+B'}
    begin = "B"
    a = 30
    def after_init(self): self.d =  max(300 / 2**self.depth,1); self.left(90)
class dragon_curve(Lindenmayer):
    rules = {'x':'x+yF', 'y': 'Fx-y'}
    begin = "Fx"
    a = 90
    def after_init(self): self.d =max( 300 / 1.5 ** self.depth, 1)
class fractal_plant(Lindenmayer):
    rules = {'X':'F-[[X]+X]+F[+FX]-X', 'F': 'FF'}
    begin = "X"
    a = 25
    def after_init(self):
        self.d = max(120 / 1.9 ** self.depth, 1)
        self.left(90)
        self.pensize(3)
if __name__ == "__main__":
    from time import sleep
    wn = turtle.Screen()
    things_to_draw = (
        (koch,3),
        (square_koch,3),
        (sierpinsky,6),
        (fibonacci_tree,5),
        (dragon_curve,10),
        (fractal_plant,5),   
    )
    for c, x in things_to_draw:
        wn.clearscreen()
        f = c()
        f.init(x)
        f.draw()
        sleep(1)
    wn.exitonclick()