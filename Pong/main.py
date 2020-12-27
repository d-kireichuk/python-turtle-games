from screen import PongScreen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from time import sleep

HEIGHT = 600
WIDTH = 800

# Game objects initialization
screen = PongScreen(height=HEIGHT, width=WIDTH).screen
ball = Ball()

p1_name = screen.textinput("Pong", "Name of first player")
p2_name = screen.textinput("Pong", "Name of second player")
score = ScoreBoard(p1_name=p1_name, p2_name=p2_name)

paddle_1 = Paddle(side="left", id=1)
paddle_2 = Paddle(side="right", id=2)

screen.update()

# Paddle key bindings
screen.listen()
screen.onkeypress(fun=paddle_1.up, key="w")
screen.onkeypress(fun=paddle_1.down, key="s")
screen.onkeypress(fun=paddle_2.up, key="Up")
screen.onkeypress(fun=paddle_2.down, key="Down")

while score.game_is_on():

    ball.move()
    sleep(ball.move_speed)
    screen.update()

    # Check for ball collision with paddles
    ball_touches_paddle = False
    for paddle in [paddle_1, paddle_2]:
        if paddle.touches_ball(ball):
            ball.bounce(obj="paddle")
            if ball.move_speed > 0.016:
                ball.move_speed -= 0.002
                print(ball.move_speed)

    # Check for ball collision with walls
    if abs(ball.xcor()) >= (WIDTH / 2):
        player = paddle_1.player_id if ball.xcor() > 0 else paddle_2.player_id
        score.update(winner=player)
        ball.reset()
    elif abs(ball.ycor()) >= HEIGHT / 2 - 20:
        ball.bounce(obj="wall")

screen.exitonclick()