from turtle import Screen
from player import Player
from car import Car
from car_manager import CarManager
from scoreboard import ScoreBoard
import time
import random


# # Uncomment to create color palette for cars
# # Replace colors.png file with color palette image you want
# # Copy printed list and paste it into Car().colors attribute in car.py
# import colorgram
# def get_colors():
#     colors = []
#     color_objects = colorgram.extract(f="colors.png", number_of_colors=8)
#     for color in color_objects:
#         colors.append(tuple(color.rgb))
#     return colors
# print(get_colors())


# Screen initialization
screen = Screen()
screen.title("Road Crossing")
screen.setup(width=600, height=600)
screen.colormode(255)
screen.mode("logo")
screen.bgcolor("light grey")
screen.tracer(0)

player = Player()
score = ScoreBoard()

# Key bindings
screen.listen()
screen.onkeypress(fun=player.go_up, key="w")
screen.onkeypress(fun=player.go_up, key="Up")

# Car objects initialization
car_manager = CarManager()

while player.is_alive(car_manager.cars):
    # Create cars at random
    car_manager.create_car()

    # Move all the cars
    # Delete a car object if it went past the screen frame
    car_manager.move_cars()

    # Check if player passed the level
    if player.ycor() >= 280:
        score.level_up()
        player.reset_position()
        # For each next level increase number of cars and car speed
        # Add extra cars each 3rd level
        car_manager.speed *= 0.95
        if score.level % 3 == 0:
            car_manager.increase_car_density()

    screen.update()
    time.sleep(car_manager.speed)

score.game_over()

screen.exitonclick()
