from turtle import Turtle

STARTING_POSITIONS = [(20, 0), (0, 0), (-20, 0)]
STEP = 20
SHAPE = "square"
COLOR = "white"

UP = 0
DOWN = 180
RIGHT = 90
LEFT = 270

class Snake:

    def __init__(self):
        self.snake = []
        self.create()
        self.head = self.snake[0]

    def add_segment(self, position):
        segment = Turtle(SHAPE)
        segment.setheading(90)
        segment.penup()
        segment.color(COLOR)
        segment.goto(position)
        self.snake.append(segment)

    def create(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            target_position = self.snake[seg_num - 1].position()
            self.snake[seg_num].goto(target_position)
        self.snake[0].forward(STEP)

    def extend(self):
        position = self.snake[-1].position()
        self.add_segment(position)

    def tail_collision(self):
        for segment in self.snake[1:]:
            if self.head.distance(segment) < 15:
                return True
        return False

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
