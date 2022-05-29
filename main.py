from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=800, height=600)
screen.bgpic("road.gif")

ALIGN = "right"
FONT = ("Courier", 20, "bold")

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
y_positions = [-260, -172, -85, 2, 85, 172, 260]
all_turtles = []

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.shapesize(1)
    new_turtle.penup()
    new_turtle.goto(x=-350, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 50)
        turtle.forward(random_distance)
        if turtle.xcor() > 350:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                turtle.write(f"You've won! The {winning_color} turtle is the winner!", font=FONT, align=ALIGN)
            else:
                turtle.write(f"You've lost! The {winning_color} turtle is the winner!", font=FONT, align=ALIGN)
            next_race = screen.textinput(title="Make your bet", prompt="Do you want to bet again?").lower()
            if next_race == "yes":
                screen.clearscreen()
                all_turtles.clear()
                screen.bgpic("road.gif")
                user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win "
                                                                          "the race? Enter a color: ")
                for turtle_index in range(0, 7):
                    new_turtle = Turtle(shape="turtle")
                    new_turtle.color(colors[turtle_index])
                    new_turtle.penup()
                    new_turtle.goto(x=-350, y=y_positions[turtle_index])
                    all_turtles.append(new_turtle)
                    random_distance = random.randint(0, 10)
                    turtle.forward(random_distance)
            else:
                is_race_on = False

screen.exitonclick()
