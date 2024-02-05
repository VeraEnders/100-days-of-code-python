import time
from turtle import Screen
from player import Player
from car import CarManager
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

score = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")

game_speed = 0.1
game_is_on = True

while game_is_on:
  time.sleep(game_speed)
  screen.update()

  car_manager.create_car()
  car_manager.move_cars()

  # Detect collision with car
  for car in car_manager.all_cars:
    if car.distance(player) < 20:
      game_is_on = False
      score.game_over()

  # Detect succesfull crossing
  if player.is_at_finish_line():
    player.go_to_start()
    car_manager.level_up()
    score.update_level()
    game_speed *= 0.9


screen.exitonclick()