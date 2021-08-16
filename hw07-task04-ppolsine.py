#!/usr/bin/python3

import random

# to create the Die class and its constructor and attributes
class Die:
    def __init__(self, sides):
        self.sides = sides
    # to create the getters and setters for the attributes
    def get_sides(self):
        return self.sides
    # to use the random module to create a random roll
    def roll(self):
        return random.randint(1, self.sides)
    # to create multiple rolls in a list
    def roll_multiple(self, rolls):
        return [random.randint(1, self.sides) for i in range(rolls)]

# to roll the die and print example output
idie = Die(20)
print(idie.get_sides())
print(idie.roll())
print(idie.roll_multiple(4))

