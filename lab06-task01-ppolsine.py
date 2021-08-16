#!/usr/bin/python3

# to define each set of inputs as a list and split for calculations
hw = list(map(int, input("Enter your hw scores: ").split(",")))
lab = list(map(int, input("Enter your lab scores: ").split(",")))
# using the split lists, perform simple calculations to find total point value of points and percentage out of 1000 possible points
total_points = sum(hw) + sum(lab)
percent = (total_points / 1000.0) * 100
# set conditional and expected output for scoring 90%
if percent > 90:
    print("You have already scored 90% or more in this class")
# perform additional calculation to find minimum points needed for 90% and print expected output
else:
    extra_credit = 1000 * 0.9 - total_points;
    print("You need at least {} points of extra credit to get a 90% in this class".format(extra_credit))