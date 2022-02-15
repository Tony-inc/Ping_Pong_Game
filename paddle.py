from turtle import Turtle

STARTING_POSITION = (350, 0)

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.setpos(position)

    def up(self):
        new_y = self.ycor() + 25
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 25
        self.goto(self.xcor(), new_y)


