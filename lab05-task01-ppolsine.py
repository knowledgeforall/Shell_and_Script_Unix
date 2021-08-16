#!/usr/bin/python3

import math

#input hypotenuse and angle B
c = float(input("Enter length of c: "))
B = float(input("Enter angle of B: "))
#calculate angle A
A = (180-90-B)
#Convert angle A and B to decimal using trigonometry formula
BB = (B*(3.14/180))
AA = (A*(3.14/180))
#calculate length a and b of the triangle
b = ((math.sin(BB)*c))
a = ((math.sin(AA)*c))
#print expected output
print("Angle A: ", A )
print("Length b: ", b)
print("Length a: ", a)