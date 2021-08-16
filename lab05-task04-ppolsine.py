#!/usr/bin/python3

import math
#recreates the menu for user to choose input
print("Number Name                           value")
print("1      Double Trouble Cheese Burger   $7.90")
print("2      Carl's Jr. Jalapeño Poppers    $8.82")
print("3      Fried Mayonnaise on a Stick    $14.53")
print("4      Danger Dog(w/ Dangerous Sauce) $9.96")
print("5      Wings                          $25.09")

#prompts for input of the user selection as a map iterator object and splits the inputs on commas
order = list(map(int, input("Please enter your order: ").split(", ")))

#calculates and prints the total cost of the order
cost = 0
for num in order:
    if num == 1:
        cost += 7.90
    elif num == 2:
        cost += 8.82
    elif num == 3:
        cost += 14.53
    elif num ==  4:
        cost += 9.96
    else:
        cost += 25.09
print("Order Total:", cost)

#sets relative money values and calculates in cents before converting, categorizing, and printing results
dollars = math.floor(cost)
pennies = round(cost * 100)
cents = pennies%100
quarters, pennies = divmod(cents, 25)
dimes, pennies = divmod(pennies, 10)
nickels, pennies = divmod(pennies, 5)
print("Dollars:", dollars)
print("Quarters:",quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)