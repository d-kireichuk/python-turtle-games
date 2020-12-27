from turtle import Turtle

X = 0
Y = 270
FONT = ("Courier", 16, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(X, Y)
        self.refresh(init=True)
        print("Scoreboard init completed.")

    def refresh(self, init=False):
        if not init:
            self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_overe(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER", align="center", font=("Courier", 30, "bold"))

