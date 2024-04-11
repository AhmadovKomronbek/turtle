from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(100)

def move_backward():
    tim.backward(100)

def move_right():
    # tim.right(90)
    new_heading = tim.heading() - 90
    tim.setheading(new_heading)

def move_left():
    # tim.left(90)
    new_heading = tim.heading() + 90
    tim.setheading(new_heading)

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")

screen.bgcolor("orange")
screen.exitonclick()
