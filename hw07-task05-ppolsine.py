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
        return random.randint(1,self.sides)
    # to create multiple rolls in a list
    def roll_multiple(self, rolls):
        return [random.randint(1, self.sides) for i in range(rolls)]
        
# to create the Coin class that inherits from Die and its constructor and attributes
class Coin(Die):
    # to create a temp object to call superclass methods with 2 sides
    def __init__(self):
        super().__init__(2)
    # to create the Die class and call roll from Die with 1 equalling heads and everything else (2) tails
    def flip(self):
        return "HEADS" if (super().roll() == 1) else "TAILS"



# to flip the nickle and print example output
nickle = Coin()
print(nickle.roll())
print(nickle.flip())
print(nickle.roll_multiple(4))