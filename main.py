from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
import winsound

scoreboard = ScoreBoard()



screen = Screen()
screen.bgpic(picname="pongtable.gif")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
game_is_on = True
winsound.PlaySound("night_train", winsound.SND_FILENAME)

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    # ball bouncing "y"axis. don't need to add "x"axis because there are only two case hit the paddle or don't and lose
    if ball.ycor() > 280 or ball.ycor() < -279:
        ball.bounce()
    # collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        winsound.PlaySound("pong1", winsound.SND_FILENAME)
        ball.collision()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.collision()
        winsound.PlaySound("pong2", winsound.SND_FILENAME)
    # Right misses the ball
    if ball.xcor() > 380:
        time.sleep(0.5)
        ball.reset_ball()
        time.sleep(0.1)
        scoreboard.clear()
        scoreboard.l_point()
        winsound.PlaySound("aaaaww", winsound.SND_FILENAME)
    # Left misses the ball
    if ball.xcor() < -380:
        time.sleep(0.5)
        ball.reset_ball()
        time.sleep(0.1)
        scoreboard.clear()
        scoreboard.r_point()
        winsound.PlaySound("aaaaww", winsound.SND_FILENAME)












screen.exitonclick()