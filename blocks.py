from turtle import Turtle
import random

blocks = []
staring = [-400, -420]
colours = ["red", "orange", "yellow", "green", "blue", "purple"]


def create_blocks():
    y = 200
    for i in range(1, 4):
        x = staring[int(i % 2)]
        while x < 430:
            torti = Turtle()
            torti.hideturtle()
            torti.penup()
            torti.color("white")
            torti.speed("fastest")
            torti.shape("square")
            torti.turtlesize(stretch_wid=1, stretch_len=3)
            torti.goto(x, y)
            torti.showturtle()
            torti.color(random.choice(colours))
            blocks.append(torti)
            x += 80
        y += 25
