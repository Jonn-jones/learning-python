import turtle
import math
import random


screen = turtle.Screen()
screen.setup(800, 700)
screen.bgcolor("black")
screen.title("A Special Message for Mary")


heart = turtle.Turtle()
heart.speed(0)
heart.hideturtle()
heart.pensize(2)

colors = ["red", "hot pink", "magenta", "purple", "cyan"]


for i in range(120):
    angle = i * 2 * math.pi / 120

    x = 16 * math.sin(angle) ** 3 * 12
    y = (
        13 * math.cos(angle)
        - 5 * math.cos(2 * angle)
        - 2 * math.cos(3 * angle)
        - math.cos(4 * angle)
    ) * 12

    heart.penup()
    heart.goto(0, 0)
    heart.pendown()
    heart.color(random.choice(colors))
    heart.goto(x, y)


text = turtle.Turtle()
text.hideturtle()
text.penup()
text.color("white")


text.goto(0, 250)
text.write(
    "I LOVE MARY",
    align="center",
    font=("Arial", 28, "bold")
)

# Display the question
text.goto(0, -230)
text.write(
    "Do you like me?",
    align="center",
    font=("Arial", 22, "bold")
)

yes = turtle.Turtle()
yes.hideturtle()
yes.penup()
yes.goto(-100, -280)
yes.color("green")
yes.dot(65)
yes.goto(-100, -290)
yes.color("white")
yes.write("YES", align="center", font=("Arial", 12, "bold"))


no = turtle.Turtle()
no.hideturtle()
no.penup()
no.goto(100, -280)
no.color("red")
no.dot(65)
no.goto(100, -290)
no.color("white")
no.write("NO", align="center", font=("Arial", 12, "bold"))


response = turtle.Turtle()
response.hideturtle()
response.penup()

def click_handler(x, y):
    response.clear()

    if -135 < x < -65 and -315 < y < -245:
        response.goto(0, -180)
        response.color("hot pink")
        response.write(
            "You made my day, Mary!",
            align="center",
            font=("Arial", 16, "bold")
        )

    elif 65 < x < 135 and -315 < y < -245:
        response.goto(0, -180)
        response.color("white")
        response.write(
            "Thank you for being honest!",
            align="center",
            font=("Arial", 14, "bold")
        )

screen.onclick(click_handler)

turtle.done()

