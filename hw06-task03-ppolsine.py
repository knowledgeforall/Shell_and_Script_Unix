#!/usr/bin/python3

# to prompt for lists 
first_list = input("Enter first list: ") # blue, green
second_list = input("Enter second list: ")# beans, bird
# to split the lists on the commas in prep for combining
firstList = first_list.split(",")
secondList = second_list.split(",")
# iterate through and combine the lists with a nested for loop
for colors in firstList:
    for nouns in secondList:
        print(colors, nouns)