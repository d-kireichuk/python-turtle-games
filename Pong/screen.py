from turtle import Screen, Turtle


class PongScreen:

    def __init__(self, height, width):
        self.mode = "logo"
        self.color = "black"
        self.height = height
        self.width = width
        self.stroke_size = 25
        self.pen_size = 4
        self.screen = self.init_screen()
        self.split_screen()

    def init_screen(self):
        screen = Screen()
        screen.title("Ping Pong")
        screen.setup(width=self.width, height=self.height)
        screen.colormode(255)
        screen.bgcolor(self.color)
        screen.mode(self.mode)
        screen.listen()
        screen.tracer(0)
        return screen

    def make_stroke(self, pen):
        y_cor = pen.ycor() - self.stroke_size
        pen.goto(0, y_cor)

    def split_screen(self):
        pen = Turtle()
        pen.hideturtle()
        pen.penup()
        pen.color("white")
        pen.pensize(self.pen_size)
        pen.goto(0, 300)
        strokes_num = int(self.height / (self.stroke_size * 2))
        for _ in range(strokes_num):
            pen.pendown()
            self.make_stroke(pen=pen)
            pen.penup()
            self.make_stroke(pen=pen)



