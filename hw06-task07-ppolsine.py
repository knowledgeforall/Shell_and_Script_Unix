#!/usr/bin/python3

# to create a function that creates a dictionary, iterates through and populates the dictionary with user inputs 'value' and 'coins'
def change (value, coins):
    dictionary = {}
    for i in range(len(coins)):
        coin_count = str(coins[i]) + " coin"
        dictionary[coin_count] = value//coins[i]
        value = round((value% coins[i]), 2)
    return dictionary
  
# to input a value, create a 'coins' list for the function, and print expected output
value = float(input("Enter a value: "))
coins = [1, 0.35, 0.23, 0.12, 0.03, 0.01]
print(change(value, coins))
