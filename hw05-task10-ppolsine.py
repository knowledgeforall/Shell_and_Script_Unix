#!/usr/bin/python3

#define list of winning numbers
winningNumbers = [29,84,8,52,89,31]

#prompt user to enter a number
num = int(input("Enter a number: "))
#if/else statement for matching and printing conditions
if num in winningNumbers:
    print(num,"is a winning number!")
else:
    print(num,"is not a winning number")