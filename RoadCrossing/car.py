from turtle import Turtle
import random
import colorgram

SHAPE = ((-5, 0), (-3, 0), (-3, 5), (3, 5), (3, 0), (5, 0), (5, -4), (3, -4),
         (3, -5), (2, -5), (2, -4), (-2, -4), (-2, -5), (-3, -5), (-3, -4), (-5, -4))


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.colors = [(204, 51, 99), (255, 103, 77), (35, 181, 211), (255, 236, 81), (255, 251, 219),
                       (205, 199, 229), (32, 6, 59), (119, 118, 188)]
        self.penup()
        self.set_car_shape()
        self.color("black")
        self.fillcolor(random.choice(self.colors))
        self.goto(x=300, y=random.randint(-220, 220))



    def set_car_shape(self):
        self.getscreen().register_shape(name="car", shape=SHAPE)
        self.shape("car")
        self.shapesize(stretch_wid=4, stretch_len=2)

    def move(self):
        self.setx(self.xcor() - 10)