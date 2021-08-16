#!/usr/bin/python3

from math import sqrt
#prompt for input and split
point1 = (input("Enter the first point without parentheses: "))
point1 = point1.split(", ")
point2 = (input("Enter the second point without parentheses: "))
point2 = point2.split(", ")
# Convert to floats
x1 = float(point1[0])
y1 = float(point1[1])
x2 = float(point2[0])
y2 = float(point2[1])
#apply formula
point_difference = (x2-x1)**2+(y2-y1)**2
distance = sqrt(point_difference)
#display expected output
print("The distance between the points ", point1, "and", point2, "is", distance)


