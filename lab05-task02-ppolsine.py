#!/usr/bin/python3

from statistics import median

values = [] #array to store names
counter=0 #counter to check number of entries
while counter<13:
    value = int(input("Enter values: ")) #taking input from the user
    counter=counter+1 #incrementing the counter variable by 1
    values.append(value) #appending the entered value to the values array
    

maximum = max(values)
minimum = min(values)
average = sum(values)/len(values)
med = median(values)
sum = sum(values)
print('Max: ', maximum)
print("Min: ", minimum)
print("Avg: ", average)
print("Med: ", med)
print("Sum: ", sum)