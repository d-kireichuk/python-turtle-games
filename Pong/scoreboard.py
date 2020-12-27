from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, p1_name, p2_name):
        super().__init__()
        self.player_score = [0, 0]
        self.player1_name = p1_name
        self.player2_name = p2_name
        self.penup()
        self.hideturtle()
        self.color("white")
        self.font = ("Courier", 60, "bold")
        self.y_cor = 0
        self.p1_x_cor = 0
        self.p2_x_cor = 0
        self.set_positions()
        self.print()
        self.winner = None

    def set_positions(self):
        screen_width = self.getscreen().window_width() / 2
        screen_height = self.getscreen().window_height() / 2
        self.y_cor = screen_height - 100
        x_cor = screen_width / 2
        self.p1_x_cor = -x_cor
        self.p2_x_cor = x_cor

    def print(self):
        self.clear()
        self.goto(self.p1_x_cor, self.y_cor)
        self.write(f"{self.player_score[0]}", font=self.font, align="center")
        self.goto(self.p2_x_cor, self.y_cor)
        self.write(f"{self.player_score[1]}", font=self.font, align="center")

    def update(self, winner):
        print("Updating score")
        if winner == 1:
            self.player_score[0] += 1
        else:
            self.player_score[1] += 1
        self.print()

    def game_is_on(self):
        for score in self.player_score:
            if score == 5:
                winner = self.player1_name if self.player_score.index(score) == 0 else self.player2_name
                self.game_over(winner)
                return False
        return True

    def game_over(self, winner):
        self.hideturtle()
        self.home()
        self.color((148, 48, 104))
        self.write(f"{winner.capitalize()} wins!",
                   font=("Arial", 30, "normal"), align="center")
        self.getscreen().update()

