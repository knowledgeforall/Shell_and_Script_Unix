#!/usr/bin/python3

import random
#prompting for input and rolling virual die
sides = int(input("Number of sides: "))
roll = random.randint(1, sides)
#display expected output
print("You rolled a", roll)