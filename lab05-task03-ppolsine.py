#!/usr/bin/python3

#prompts for input of the string as a map iterator object and splits the inputs on commas
names = list(map(str, input().split(",")))

#corrects and changes names to sort in proper order
names[1] = "The Humans"
names[2] = "Demon Days"
names.remove("Face Value")
names[4] = "Plastic Beach"
names.sort()

#makes last correction and prints list
names[3] = "Humanz"
print(names)