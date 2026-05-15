
from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("./highscore.txt", mode="r") as file:
            highscore=file.read()
        self.score=0
        self.hideturtle()
        self.color("white");self.penup();self.goto(0,260)
        self.write(f"Score: {self.score} High Score:{highscore}",False,"center",("Arial",24,"normal"))

    def change_score(self):
        self.clear()
        self.score+=1
        with open("./highscore.txt", mode="r") as file:
            self.write(f"Score: {self.score}  High Score:{file.read()}",False,"center",("Arial",24,"normal"))

    def reset_high_score(self):
        with open("./highscore.txt", mode="r") as file:
            if self.score>int(file.read()):
                with open("./highscore.txt",mode="w") as file:
                    file.write(str(self.score))

    def game_over(self):
        self.home()
        self.write("Game Over",False,"center",("Arial",24,"normal"))


