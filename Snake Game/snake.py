from turtle import Turtle
class Snake:
    def __init__(self, number):
        self.segments = []
        self.create_snake(number)
        self.segments[0].color("green")

    def create_snake(self, body):
        for i in range(body):
            self.tuzik = Turtle()
            self.tuzik.shape("square")
            self.tuzik.penup()
            self.tuzik.setposition(-20 * i, 0)
            self.tuzik.color("white")
            self.segments.append(self.tuzik)

    def move(self):
        for item in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[item - 1].xcor()
            new_y = self.segments[item - 1].ycor()
            self.segments[item].goto(new_x, new_y)
        self.segments[0].forward(20)
        # self.segments[0].left(90)

    def up(self):
        if self.segments[0].heading()!=270:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading()!=90:
            self.segments[0].setheading(270)
    def left(self):
        if self.segments[0].heading()!=0:
            self.segments[0].setheading(180)
    def right(self):
        if self.segments[0].heading()!=180:
            self.segments[0].setheading(0)

    def add_body(self):
        self.tuzik = Turtle()
        self.tuzik.shape("square")
        self.tuzik.penup()
        self.tuzik.color("white")
        self.tuzik.goto(self.segments[len(self.segments)-1].xcor(), self.segments[len(self.segments)-1].ycor())
        self.segments.append(self.tuzik)