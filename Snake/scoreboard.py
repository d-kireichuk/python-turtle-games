from turtle import Turtle
import time

X = 0
Y = 270
FONT = "Segoe UI"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.get_high_score()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.refresh(init=True)

    def get_high_score(self):
        with open("high_score.txt") as f:
            self.high_score = int(f.read())

    def refresh(self, init=False):
        if not init:
            self.score += 1
        self.clear()
        self.color("white")
        self.goto(X, Y)
        self.write(f"Score: {self.score}    High Score: {self.high_score}",
                   align="center", font=(FONT, 16, "normal"))

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as f:
                f.write(f"{self.high_score}")
            return "\nNew record!"
        return ""

    def reset(self):
        self.goto(0, 0)
        self.color("purple")
        new_record = self.update_high_score()
        self.write(f"GAME OVER{new_record}", align="center", font=(FONT, 20, "normal"))
        self.score = 0
        time.sleep(1.7)
        self.refresh(init=True)