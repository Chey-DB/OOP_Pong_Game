from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, positions):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setpos(positions)
        self.setheading(90)

    def paddle_up(self):
        self.forward(20)

    def paddle_down(self):
        self.backward(20)

