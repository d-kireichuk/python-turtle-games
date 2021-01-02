from turtle import Turtle
import pandas


class GameManager(Turtle):

    def __init__(self):
        super().__init__()
        self.data = pandas.read_csv("50_states.csv")
        self.all_states = self.data.state.to_list()
        self.states_to_guess = self.data.state.to_list()
        self.guessed_states = 0
        self.penup()
        self.hideturtle()

    def is_game_on(self):
        if len(self.states_to_guess) == 0:
            self.home()
            self.write("Congratulations!", align="center", font=("Segoe UI", 16, "bold"))
            return False
        return True

    def validate_state(self, user_input):
        state = user_input.title()
        if state not in self.all_states or state not in self.states_to_guess:
            return
        state_data = self.data[self.data.state == state]
        coordinate = (state_data.x.item(), state_data.y.item())
        self.goto(coordinate)
        self.write(state_data.state.item(), align="center")
        self.states_to_guess.remove(state)
        self.guessed_states += 1

    def export_states_to_learn(self):
        states_to_learn = pandas.DataFrame(self.states_to_guess)
        states_to_learn.to_csv("states_to_learn.csv", header=False, index=False)