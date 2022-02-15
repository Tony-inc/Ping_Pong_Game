from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("THE PING PONG GAME")
screen.tracer(0)

ball = Ball()
score = Score()


game_on = True
paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))


screen.listen()
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")


while game_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    # Detect collision with the walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the side walls
    if ball.xcor() > 390:
        ball.reset_position()
        score.l_goal()

    if ball.xcor() < -390:
        ball.reset_position()
        score.r_goal()

    # Detect collision with the paddles
    if ball.xcor() > 320 and ball.distance(paddle_r) < 50 or ball.xcor() < -320 and ball.distance(paddle_l) < 50:
        ball.bounce_x()
































screen.exitonclick()