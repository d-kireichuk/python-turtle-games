from turtle import Turtle

START_POS = (0, -280)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.reset_position()
        self.fillcolor("green")

    def reset_position(self):
        self.goto(START_POS)

    def go_up(self):
        self.sety(self.ycor() + 10)

    def is_alive(self, cars=[]):
        for car in cars:
            if self.distance(car) <= 25:
                return False
        return True
