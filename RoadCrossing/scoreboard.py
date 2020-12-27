from turtle import Turtle

FONT = "Segoe UI"

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.refresh_level()

    def refresh_level(self):
        self.clear()
        self.goto(-220, 250)
        self.write(f"Level {self.level}", align="center", font=(FONT, 22, "normal"))

    def level_up(self):
        self.level += 1
        self.refresh_level()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=(FONT, 30, "bold"))
        self.getscreen().update()
