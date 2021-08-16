#!/usr/bin/python3

#prompt to enter total
subtotal = float(input("Enter the total: "))

#enter tip amount and compute
tipPercent = 15
tip = (tipPercent/100)*subtotal

#compute total
total = subtotal + tip
#print the expected output with tip and total to two decimal places
print("A {}% tip on {} would be {:.2f}. The total would be {:.2f}".format(tipPercent,subtotal,tip,total))