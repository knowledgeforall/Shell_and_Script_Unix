#!/usr/bin/python3

# to set count to keep while loop constant.  Could also use while true
count = 1
cost = 14.85
# to create a simple subtraction function that outputs to 2 decimal places
def difference():
    diff = cost - cash
    diff_formatted = "{:.2f}".format(diff)
    return diff_formatted
# to keep the prompt recurring
while count > 0:
    # to input a number to input into the difference function
    cash = (float(input("Enter a number: ")))
    # to create the conditionals for what to output
    if cash == cost:
        print("That is exactly enough")
    elif cash < cost:
        print("That is not enough by ", difference())
    elif cash > cost:
        print("There is change due of ", difference())