from turtle import Turtle
import random

"""Step4: make the food class a sub-class of turtle, this is used to make the food """
"""4b: now we go to our main.py where we will write the code to check if the snake has come in contact with the food """
"""4c: then we make a method called refresh in the food-class then we make an if statement in the main and call it   """


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
