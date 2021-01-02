from turtle import Screen
from game_manager import GameManager

screen = Screen()
screen.title("US States Guessing Game")
screen.setup(width=725, height=491)
screen.bgpic(picname="blank_states_img.gif")
gm = GameManager()

while gm.is_game_on():
    input = screen.textinput(title=f"{gm.guessed_states}/50 states correct", prompt="Enter a US state name: ")
    if input == "exit":
        gm.export_states_to_learn()
        screen.bye()
        exit()
    gm.validate_state(input)

screen.exitonclick()
