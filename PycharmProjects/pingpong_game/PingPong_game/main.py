from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Ping Pong game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
pong = Ball()
# To avoid repeated bounces
paddle_hit = 0
score = Scoreboard()


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(pong.ball_speed)
    screen.update()
    pong.move()

    # detect when the ball hits the wall
    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce_y()

    # detect collision with paddle
    if paddle_hit == 0:
        if pong.distance(r_paddle) < 50 and pong.xcor() > 320 or pong.distance(l_paddle) < 50 and pong.xcor() < -320:
            pong.bounce_x()
            paddle_hit = 1
    else:
        if -320 < pong.xcor() < 320:
            paddle_hit = 0
            
    # detect when ball misses r_paddle and give l a point
    if pong.xcor() > 380:
        pong.switch_player()
        score.l_point()

    # detect when ball misses l_paddle give r a point
    if pong.xcor() < -380:
        pong.switch_player()
        score.r_point()
screen.exitonclick()
