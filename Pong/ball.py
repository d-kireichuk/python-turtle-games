from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color((148, 48, 104))
        self.penup()
        self.shape("circle")
        self.speed("fastest")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    def reset(self):
        self.goto(0, 0)
        self.bounce()

    def bounce(self, obj="paddle"):
        if obj == "wall":
            self.y_move *= -1
        elif obj == "paddle":
            self.x_move *= -1

    def move(self):
        self.showturtle()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
