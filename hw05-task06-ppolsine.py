#!/usr/bin/python3

#preloaded strings
name = "Shaun, Sammy, Brandon, Arielle, Erik, Steven"
grade = "89, 97, 47, 99, 69, 94"
#create list from strings with split
nameList = name.split(", ")
gradeList = grade.split(", ")
#create dictionary, populate with name list values, and equate to corresponding grade list values
dictionary ={}
index =0
while(index < len(nameList)):
    dictionary[nameList[index]]=gradeList[index]
    index+=1
#prompting for name and displaying expected output
nameinput = input("Enter a name:")
print(f"{nameinput}: {dictionary[nameinput]}")