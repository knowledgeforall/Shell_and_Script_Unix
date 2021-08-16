#!/usr/bin/python3

# to create a function that creates a dictionary, iterates through and populates the dictionary with user inputs 'value' and 'coins'
def change (value, coins):
    dictionary = {}
    for i in range(len(coins)):
        coin_count = str(coins[i]) + " coin"
        dictionary[coin_count] = int(value//coins[i])
        value = round((value% coins[i]), 2)
    return dictionary

# to get inputs for the funcion, splitting one of the inputs on commas for the dictionary
value = float(input("Enter a value : "))
coins = [float(num) for num in input("Enter coins : ").split(",")]
# to call the function and print the expected output
print(change(value,coins))