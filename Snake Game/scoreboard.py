from turtle import Turtle
from snake import Snake

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.setposition(-150,250)
        self.show_score()
        self.hideturtle()
        self.record=0



    def show_score(self):
        with open("record.txt",  mode="r") as file:
            self.record=int(file.read())

        self.clear()
        self.write(f"Score: {self.score} Record: {self.record}", font=('Courier', 24, 'normal'))

    def update_score(self):
        self.score+=1
        self.show_score()

    def rewrite_record(self):
        if self.score>self.record:
            with open("record.txt", mode="w") as file:
                file.write(str(self.score))
