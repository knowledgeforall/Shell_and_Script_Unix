#!/usr/bin/python3

import math

#set rate and time
r = 1
t = 1
#create dictionary
dictionary = {}
#prompt for initial value and set as principal
print("Enter a starting value: ")
P = int(input())
#create loop to decide to print year or years
for num in range(1, 11):
    yearNumber = ""
    if num == 1:
        number = str(num)
        yearNumber = number + " year"
    else:
        number = str(num)
        yearNumber = number + " years"
#apply formula to calculate compounding interest    
    amount = P * (pow((1 + r / 100), t)) 
    compInterest = amount - P
    P = P + compInterest
    P = math.ceil(P)
    dictionary[yearNumber] = P
#print expexted output    
for key in dictionary:
    print(key, ":", dictionary[key])