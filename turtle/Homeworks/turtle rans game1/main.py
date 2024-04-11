from turtle import Turtle, Screen
from random import randint

def play():
    screen = Screen()
    screen.setup(800, 600)
    tom = Turtle()
    tom.hideturtle()
    tom.speed("fastest")
    tom.penup()
    tom.color("grey")
    tom.goto(x=-400, y=100)
    tom.pendown()
    tom.begin_fill()
    tom.goto(x=400, y=100)
    tom.goto(x=400, y=60)
    tom.goto(x=-400, y=60)
    tom.end_fill()

    tom.penup()
    tom.goto(x=-400, y=20)
    tom.pendown()
    tom.begin_fill()
    tom.goto(x=400, y=20)
    tom.goto(x=400, y=-20)
    tom.goto(x=-400, y=-20)
    tom.end_fill()

    tom.penup()
    tom.goto(x=-400, y=-60)
    tom.pendown()
    tom.begin_fill()
    tom.goto(x=400, y=-60)
    tom.goto(x=400, y=-100)
    tom.goto(x=-400, y=-100)
    tom.end_fill()

    colors = ["red", "blue", "yellow"]

    is_race_on = False
    user_choose = ""

    while True:
        user_choose += screen.textinput("what is tour choice", "which turtle will win the race?(Enter only color)")
        if user_choose in colors:
            break
        else:
            continue

    all_turtles = []

    y_position = 80
    for i in range(3):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[i])
        new_turtle.shapesize(stretch_wid=2, stretch_len=2, outline=8)
        new_turtle.penup()
        new_turtle.goto(x=-400, y=y_position)
        y_position -= 80
        all_turtles.append(new_turtle)

    if user_choose:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() >= 370:
                is_race_on = False
                winning_color = turtle.pencolor()
                message = ""
                if winning_color == user_choose:
                    message += "You win"
                    screen.clear()
                    screen.bgpic("you_win.png")
                else:
                    message += "You lose"
                    screen.clear()
                    screen.bgpic("you_lost.png")

                play_again = screen.textinput(title=message, prompt="play again").lower()
                if play_again == "yes":
                    play()
                else:
                    exit()
            turtle.pendown()
            turtle.pensize(10)
            random_distance = randint(0, 10)
            turtle.forward(random_distance)
            print(turtle.ycor())

    screen.exitonclick()

play()
