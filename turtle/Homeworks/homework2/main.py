import turtle as t
a = t.Turtle()

a.color("brown")
a.forward(200)
a.left(90)
a.forward(120)
a.left(90)
a.forward(200)
a.left(90)
a.forward(120)
a.left(90)

a.penup()
a.forward(25)
a.left(90)
a.pendown()
a.forward(85)
a.right(90)
a.forward(40)
a.right(90)
a.forward(85)

a.penup()
a.left(180)
a.forward(40)
a.pendown()
a.left(90)
a.forward(10)
a.right(90)
a.forward(5)
a.right(90)
a.forward(10)
a.right(90)
a.forward(45)

a.penup()
a.left(90)
a.forward(40)
a.left(90)
a.forward(45)
a.right(90)
a.pendown()
a.forward(50)
a.left(90)
a.forward(40)
a.left(90)
a.forward(50)
a.left(90)
a.forward(40)
a.left(90)
a.forward(25)
a.left(90)
a.forward(40)
a.left(90)
a.forward(25)
a.left(90)
a.forward(20)
a.left(90)
a.forward(50)

a.penup()
a.forward(45)
a.left(90)
a.forward(55)
a.left(45)
a.pendown()
a.color("grey")
a.forward(141)
a.left(90)
a.forward(141)
a.left(45)
a.penup()
a.forward(120)

a.pendown()
a.color("green")
a.right(90)
a.forward(500)
a.left(180)
a.forward(1000)

a.penup()
a.left(180)
a.forward(750)
a.right(90)
a.forward(200)
a.pendown()
a.color("yellow")
a.begin_fill()
a.circle(50)
a.end_fill()

a.color("brown")
a.penup()
a.right(180)
a.forward(200)
a.left(90)
a.forward(100)
a.left(90)
a.pendown()
a.forward(75)

a.color("green")
a.begin_fill()
a.circle(25)
a.end_fill()
a.right(90)
a.begin_fill()
a.circle(25)
a.end_fill()

a.right(90)
a.begin_fill()
a.circle(25)
a.end_fill()
a.color("brown")
a.forward(75)


screen = t.Screen()
screen.exitonclick()