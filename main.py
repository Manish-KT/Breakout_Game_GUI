from turtle import Screen
from paddle import Paddle
from ball import Ball
from blocks import create_blocks, blocks
import time

# 1. create a screen
paddle = Paddle()
ball = Ball()
screen = Screen()
# scoreboard = Scoreboard()
speed = 0.05

screen.bgcolor("black")
screen.setup(width=900, height=610)
screen.title("Retro Ping-Pong Game :>)")

# 2. create and move a paddle.
screen.listen()
paddle.create_paddle()
screen.onkey(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")

# 3. detect collision with ball
game_on = True
ball.make_ball()


# add blocks
create_blocks()


while game_on:
    for block in blocks:
        if ball.torti.distance(block) < 20:
            color = block.color()[0]
            ball.change_color(color)
            blocks.remove(block)
            block.hideturtle()
            ball.bounce_y()

    time.sleep(speed)
    screen.update()
    ball.start()

    # collision with right and left wall
    if ball.ball_x > 420 or ball.ball_x < -420:
        ball.bounce_x()

    # 4. detect collision with right paddle
    # 5. detect collision when paddle misses
    if ball.ball_y > 280:
        ball.bounce_y()

    elif ball.torti.distance(paddle.board) < 20:
        ball.bounce_y()
        speed *= 0.9

    elif ball.ball_y < -280:
        ball.reset()

    if len(blocks) == 0:
        ball.reset()
        speed *= 9

# 6. keep track of score
screen.exitonclick()
