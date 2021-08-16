#!/usr/bin/python3

# to input strings and create a dictionary
names = input("Enter names : ")# Shaun, Sammy, Brandon, Arielle, Erik, Steven
grades = input("Enter grades : ")# 89, 97, 47, 99, 69, 94
dictionary = {}
# to split strings into separate list inputs without using the maps method to ready to insert into dictionary
names = names.split(",")
grades = grades.split(",")
# to iterate through the splits and insert them into dictionary, stripping out the blank spaces for esthetics
for i in range(len(names)):
    dictionary[names[i].strip()] = grades[i].strip()
    # to print the expected output
print(dictionary)

