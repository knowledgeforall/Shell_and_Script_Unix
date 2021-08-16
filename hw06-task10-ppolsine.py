#!/usr/bin/python3

# to import the module to create a psuedo random cost
import random
# to create a continuous running of the script
while True:
    # to create a random number with two inputs starting at 1 and ending at 100 to two decimal places and print it
    cost = round(random.uniform(1, 100), 2)
    print("Cost is {}".format(cost))
    # to prompt for payment input and end 'while True' block, sending script to last print line 'Goodbye'.
    payment = input("Enter a payment: ")
    if payment == "quit":
        break
        #to check for proper input type and print a corrective statement if necessary
    try:
        # to convert payment variable to a float for math operations. could not make input a float because break function would not work for some reason.
        payment = float(payment)
        # to input the coin denomination string to input into the 'coins' list
        coins = list(set(map(float, input("Enter a list of coin values: ").split(","))))
    except:
        print("Only digits in the correct format can be entered.  Please try again.")
        continue
    # to calculate if change is due and generate proper response
    change_due = cost - payment
    # to create conditionals for whether change is due or not, or more money is needed
    # 'end' parameter used to keep ouput on same line as print statement
    if change_due == 0:
        print("No change due")
    elif (change_due > 0):
        print("needed: ", end="")
    else:
        print("change: ", end="")
     
    if(change_due != 0):
        coins.sort(reverse = True)
        
        coin_count = {}
        
        change_due = abs(change_due)
        change_due = change_due*100//1
        
        for i in coins:
            if change_due//(i*100) != 0:
                coin_count[i] = int(change_due//(i*100))
                change_due = change_due - ((i*100) * (change_due//(i*100)))

        if change_due != 0:
            print("Change not possible with the given coins")
            continue
          
        for i in coin_count:
            print("{} {} coins,".format(coin_count[i], i), end=" ")

print("Goodbye!")