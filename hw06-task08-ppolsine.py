#!/usr/bin/python3

# to create a function that creates a dictionary, iterates through and populates the dictionary with user inputs 'value' and 'coins'
def change (payment, coins):
    dictionary = {}
    for i in range(len(coins)):
        coin_count = str(coins[i])+" coin"
        dictionary[coin_count] = payment//coins[i]
        payment = round((payment% coins[i]), 2)
    return dictionary

# to create input, 'coins' list, and calculate change
payment = float(input("Enter your payment : "))
coins = [1, 0.35, 0.23, 0.12, 0.03, 0.01]
difference = (16.48 - payment)
# to create conditions for change or no change, or needing more money, and printing expected output
if (payment > 16.48):
    print("Change", end=" ")
    dictionary = change(difference, coins)
    for i in dictionary:
        print(int(dictionary[i]), i, end=", ")
elif (payment == 16.48):
    print("No change due")
else:
    print("Needed", end=" ")
    dictionary = change(difference, coins)
    for i in dictionary:
        print(int(dictionary[i]), i, end=", ")