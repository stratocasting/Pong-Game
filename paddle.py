from turtle import Turtle, Screen
screen = Screen()


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("brown3")
        self.shapesize(5.1, 0.9)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 35
        self.goto(x=self.xcor(), y=new_y)

    def go_down(self):
        new_y = self.ycor() - 35
        self.goto(x=self.xcor(), y=new_y)
