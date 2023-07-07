import turtle
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):  # STEP 1: CREATE THE SNAKE
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # Step 5: we will move the segment of the snake in step 1 into add segment.then call add_segment in
        # create_snake.
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        # add a new segment to the snake to make it longer after it eats food.
        self.add_segment(self.segments[-1].position())

    def move(self):  # STEP 2: MOVE THE SNAKE
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):  # STEP 3: CONTROL THE SNAKE
        if self.head.heading() != DOWN:  # if the snake is not facing down; then the snake can go up.
            self.head.setheading(UP)  # to avoid hitting itself

    def down(self):  # STEP 3: CONTROL THE SNAKE
        if self.head.heading() != UP:  # if the snake is not facing up; then the snake can go down.
            self.head.setheading(DOWN)  # to avoid hitting itself

    def left(self):  # STEP 3: CONTROL THE SNAKE
        if self.head.heading() != RIGHT:  # if the snake is not facing right; then the snake can go left.
            self.head.setheading(LEFT)  # to avoid hitting itself

    def right(self):  # STEP 3: CONTROL THE SNAKE
        if self.head.heading() != LEFT:  # if the snake is not facing left; then the snake can go right.
            self.head.setheading(RIGHT)  # to avoid hitting itself
