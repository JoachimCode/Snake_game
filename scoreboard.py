from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 250)
        self.hideturtle()
        self.write(f"Your score is {self.score}", False, "center", ("Arial", 12, "normal"))

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Your score is {self.score}", False, "center", ("Arial", 12, "normal"))

    def game_over(self):
        self.goto(0, 150)
        self.write("You lost", False, "center", ("Arial", 24, "normal"))