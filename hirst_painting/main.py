import random
import colorgram
from turtle import Turtle, Screen

CIRCLE_RADIUS = 10
DISTANCE = 50
CIRCLES_PER_ROW = 10
CIRCLES_PER_COL = 10

colors = colorgram.extract('image.jpg', 34)
colors_list = [tuple(color.rgb)for color in colors if color.proportion < 0.01]


def draw_circle(turtle_obj):
    turtle_obj.color(random.choice(colors_list))
    turtle_obj.begin_fill()
    turtle_obj.circle(CIRCLE_RADIUS)
    turtle_obj.end_fill()


screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.speed(0)
tim.hideturtle()
start_row = -(CIRCLE_RADIUS + (CIRCLES_PER_ROW - 1) * DISTANCE) / 2
start_col = -(CIRCLE_RADIUS + (CIRCLES_PER_COL - 1) * DISTANCE) / 2

for row in range(CIRCLES_PER_ROW):
    for col in range(CIRCLES_PER_COL):
        tim.teleport(start_col + col * DISTANCE, start_row + row * DISTANCE)
        draw_circle(tim)

screen.exitonclick()
