from turtle import Turtle


class Paddle:

    def __init__(self):
        self.board = None
        self.move = 0

    def create_paddle(self):
        torti = Turtle()
        torti.penup()
        torti.color("white")
        torti.speed("fastest")
        torti.shape("square")
        torti.turtlesize(stretch_wid=5, stretch_len=1)
        torti.right(90)
        self.board = torti
        self.board.goto(0, -280)

    def move_left(self):
        if self.move > -350:
            self.move = self.move - 15
            self.board.goto(self.move, -280)

    def move_right(self):
        if self.move < 350:
            self.move = self.move + 15
            self.board.goto(self.move, -280)

