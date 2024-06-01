from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")
HIGH_SCORE_FILE = "data.txt"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = None
        self.score = 0
        self.read_high_score()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_scoreboard()

    def read_high_score(self):
        with open(HIGH_SCORE_FILE, "r") as f:
            self.high_score = int(f.read())

    def write_high_score(self):
        with open(HIGH_SCORE_FILE, "w") as f:
            f.write(str(self.high_score))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
