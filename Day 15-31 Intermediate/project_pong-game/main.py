from turtle import Screen
from score import Score
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

score = Score()
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

game_is_on = True

while game_is_on:
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()

  # Detect collision with wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  # Detect collision with right_paddle
  if ball.distance(right_paddle) < 50 and ball.xcor() > 320: 
    ball.bounce_x()
   
  # Detect collision with left_paddle
  if ball.distance(left_paddle) < 50 and ball.xcor() < -320: 
    ball.bounce_x()

  # Detect right_paddle misses
  if ball.xcor() > 380:
    ball.reset_position()
    score.increase_l_score()

  # Detect left_paddle misses
  if ball.xcor() < -380:
    ball.reset_position()
    score.increase_r_score()

screen.exitonclick()