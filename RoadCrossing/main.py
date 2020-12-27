from turtle import Screen
from player import Player
from car import Car
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

# Key bindings
screen.listen()
screen.onkeypress(fun=player.go_up, key="w")
screen.onkeypress(fun=player.go_up, key="Up")

# Car objects initialization
cars = [Car()]
car_speed = 0.1
score = ScoreBoard()
cars_num = 1
loop_count = 0

while player.is_alive(cars):
    # Create a random number of cars
    loop_count += 1
    if loop_count == 5:
        for _ in range(random.randint(0, cars_num)):
            cars.append(Car())
        loop_count = 0

    # Move all cars
    # Delete a car object if it went past the screen frame
    for car in cars:
        car.move()
        if car.xcor() < -300:
            car.hideturtle()
            cars.remove(car)

    # Check if player passed the level
    if player.ycor() >= 280:
        score.level_up()
        player.reset_position()
        # For each next level increase number of cars and car speed
        car_speed *= 0.95
        if score.level % 3 == 0:
            cars_num += 1

    screen.update()
    time.sleep(car_speed)

score.game_over()

screen.exitonclick()
