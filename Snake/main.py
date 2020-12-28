from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from time import sleep

HEIGHT = 600
WIDTH = 600

# Screen configurations
screen = Screen()
screen.setup(height=HEIGHT, width=WIDTH)
screen.mode("logo")
screen.colormode(255)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(fun=snake.turn_up, key="Up")
screen.onkey(fun=snake.turn_down, key="Down")
screen.onkey(fun=snake.turn_right, key="Right")
screen.onkey(fun=snake.turn_left, key="Left")

game_is_on = True
screen.update()

while game_is_on:
    snake.move()
    screen.update()

    # Detect collision with the food
    found_food = True if snake.head.distance(food) <= 15 else False
    if found_food:
        snake.extend()
        food.refresh()
        scoreboard.refresh()

    # Detect collision with the tail or the walls
    if snake.tail_collision() or snake.wall_collision():
        scoreboard.reset()
        snake.reset()

    sleep(0.085)



screen.exitonclick()