import turtle

tr = turtle.Turtle()

def draw_thing(func):
    tr.penup()
    func()
    tr.pendown()

tr.color('yellow')
tr.begin_fill()
tr.circle(150)
tr.end_fill()

tr.color('black')
draw_thing(lambda: tr.goto(-50, 175))
tr.circle(25)
draw_thing(lambda: tr.goto(50, 175))
tr.circle(25)

draw_thing(lambda: tr.goto(-60, 60))
tr.setheading(315)
tr.width(10)
tr.circle(90, 90)


turtle.mainloop()