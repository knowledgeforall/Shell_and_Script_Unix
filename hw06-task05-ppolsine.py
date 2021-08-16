#!/usr/bin/python3

# to input animals string and split
animals = input("Enter animals string: ").split(",")
# to create empty list with split animals string and append to list with iteration
animal_list = []
for animal in animals:
    animal_list.append("hello, "+animal.strip()+"!")
# to print expected output
print(animal_list)