from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.show_score()

    def show_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="left", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="right", font=("Courier", 80, "normal"))

    def l_goal(self):
        self.l_score += 1
        self.show_score()

    def r_goal(self):
        self.r_score += 1
        self.show_score()
