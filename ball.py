from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("DarkGoldenrod1")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce(self):
        self.y_move *= -1

    def collision(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0,0)








