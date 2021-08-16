#!/usr/bin/python3

# to enter animal names
animals = input("Enter animals name: ")
# to create list and populate with input
animals_list = animals.split(",")
# to create iteration of list and apply text
greet_animals = [ "hello," + animal + "!" for animal in animals_list]
# to print expected output
print(greet_animals)