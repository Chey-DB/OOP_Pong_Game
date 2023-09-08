from turtle import Turtle
LEFT_POSITIONS = [(-480, 20), (-480, 0), (-480, -20)]
RIGHT_POSITIONS = [(480, 20), (480, 0), (480, -20)]


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_left_paddle()
        self.create_right_paddle()
        self.top = self.segments[0]
        self.bottom = self.segments[2]

    def create_left_paddle(self):
        for position in LEFT_POSITIONS:
            self.add_segment(position)

    def create_right_paddle(self):
        for position in RIGHT_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.segments.append(snake)

    def up(self):
        self.forward(5)

    def down(self):
        self.backward(5)

    def create_left_paddle(self):
        lpad = Turtle(shape="square")
        lpad.color("white")
        lpad.penup()
        lpad.shapesize(stretch_wid=1, stretch_len=4)
        lpad.setpos(LEFT_POSITIONS)
        lpad.setheading(90)

    def create_right_paddle(self):
        rpad = Turtle(shape="square")
        rpad.color("white")
        rpad.penup()
        rpad.shapesize(stretch_wid=1, stretch_len=4)
        rpad.setpos(RIGHT_POSITIONS)
        rpad.setheading(90)

    self.create_left_paddle()
    self.create_right_paddle()

