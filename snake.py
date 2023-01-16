from turtle import Turtle, Screen

STARTING_POSITION = [(-10, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.shape("square")
        snake.speed(5)
        snake.goto(position)
        self.segments.append(snake)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def move_up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def move_left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def move_down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def move_right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
