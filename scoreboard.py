from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.display()

    def display(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.display()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)