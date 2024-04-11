from turtle import Turtle, Screen
from random import randint

def play():
    screen = Screen()
    screen.setup(800, 600)

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
                else:
                    message += "You lose"

                play_again = screen.textinput(title=message, prompt="play again").lower()
                if play_again == "yes":
                    screen.clear()
                    play()
                else:
                    exit()
            random_distance = randint(0, 10)
            turtle.forward(random_distance)

    screen.exitonclick()

play()
