import turtle as t
draw_turtle = t.Turtle()

def draw_squares(a):
    for _ in range(4):
        draw_turtle.forward(a)
        draw_turtle.left(90)

def draw_rectangles(a, b):
    for _ in range(2):
        draw_turtle.forward(a)
        draw_turtle.left(90)
        draw_turtle.forward(b)
        draw_turtle.left(90)

def draw_triangles(a):
    for _ in range(3):
        draw_turtle.forward(a)
        draw_turtle.left(120)

def draw_circles(a):
    draw_turtle.circle(a)

draw_squares(100)
draw_rectangles(100, 200)
draw_triangles(100)
draw_circles(100)

screen = t.Screen()
screen.exitonclick()
