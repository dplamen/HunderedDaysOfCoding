from turtle import Turtle, Screen
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_shape(sides, turtle_obj):
    turtle_obj.pencolor(random_color())
    angle = 360 / sides
    for _ in range(sides):
        turtle_obj.forward(100)
        turtle_obj.right(angle)


def random_move(turtle_obj):
    turtle_obj.pencolor(random_color())
    turtle_obj.width(15)
    turtle_obj.speed(0)
    direction = random.choice([90, 180, 270, 360])
    turtle_obj.left(direction)
    turtle_obj.forward(50)


def draw_circle(turtle_obj):
    turtle_obj.color(random_color())
    turtle_obj.speed(0)
    turtle_obj.circle(100)


tim = Turtle()
screen = Screen()
screen.colormode(255)
# for shape in range(3, 11):
#     draw_shape(shape, tim)

# for _ in range(150):
#     random_move(tim)

for degrees in range(0, 360, 5):
    tim.speed(5)
    draw_circle(tim)
    tim.setheading(degrees)


screen.exitonclick()
