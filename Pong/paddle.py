from turtle import Turtle
from time import sleep

STEP = 20


class Paddle(Turtle):

    def __init__(self, side, id):
        super().__init__()
        self.player_id = id
        self.x_pos = 0
        self.init_paddle(side)

    def init_paddle(self, side):
        self.x_pos = ((self.getscreen().window_width() / 2) - 20)
        if side == "left":
            self.x_pos *= -1
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=5)
        self.goto(self.x_pos, 0)

    def up(self):
        if self.ycor() >= (self.getscreen().window_height() / 2) - 50:
            return
        self.goto(self.x_pos, self.ycor() + STEP)

    def down(self):
        if self.ycor() <= -(self.getscreen().window_height() / 2) + 75:
            return
        self.goto(self.x_pos, self.ycor() - STEP)

    def touches_ball(self, ball):
        if self.distance(ball) <= 50 and abs(ball.xcor()) > 350:
            return True
        return False

