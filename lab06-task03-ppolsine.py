#!/usr/bin/python3
# to import random module for psuedo random number generation
import random
# to create maximum number for random generator to create
sides = int(input("Enter number of sides: "))
# conditional to ensure a number greater than zero is input
if(sides < 1):
   print("Must be greater than zero.  Try again.")
# to initiate random number generation and print expected output
else:
   roll = random.randint(1, sides)
   print("Roll: ", roll)