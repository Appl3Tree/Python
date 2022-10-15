import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=650, height=650)
screen.screensize(canvwidth=600, canvheight=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, 'Up')

loop = 1
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Every 6 loops, add a new car.
    if loop % 6 == 0:
        car_manager.create_car()
    car_manager.move_cars()

    # If player gets across safely, then move to next level.
    if player.go_to_next_level():
        scoreboard.update_level()
        player.next_level()
        car_manager.level_up()

    # If player hits a car, then game over.
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    loop += 1

screen.exitonclick()
