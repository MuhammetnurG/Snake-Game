from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed("fastest")
        coor_x=random.randint(-280,280)
        coor_y=random.randint(-280,280)
        self.goto(coor_x, coor_y)

    def go_somewhere(self):
        coor_x=random.randint(-280,280)
        coor_y=random.randint(-280,280)
        self.goto(coor_x, coor_y)