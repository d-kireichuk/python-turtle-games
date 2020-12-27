from turtle import Turtle
import random
import colorgram

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.colors = []
        self.set_colors()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)

        self.speed(0)
        self.refresh()

    def set_colors(self):
        color_objects = colorgram.extract(f="food_colors.png", number_of_colors=5)
        for color in color_objects:
            self.colors.append(tuple(color.rgb))

    def refresh(self):
        rand_color = random.choice(self.colors)
        self.color(rand_color)
        rand_x = random.randint(-250, 250)
        rand_y = random.randint(-250, 250)
        self.goto(rand_x, rand_y)
