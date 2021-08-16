#!/usr/bin/python3

#preloaded strings
name = "Shaun, Sammy, Brandon, Arielle, Erik, Steven"
grade = "89, 97, 47, 99, 69, 94"
#create list from strings with split
nameList = name.split(", ")
gradeList = grade.split(", ")
#get input and print expected output
index = int(input("Enter an entry: "))
print(f"{nameStringList[index]}: {gradeStringList[index]}")