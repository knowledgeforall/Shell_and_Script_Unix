#!/usr/bin/python3

# module that allows reading and writing to csv file
import csv
# to input a name
name = input("Enter a name: ")

# to open the csv file to be able to search it
with open('lab0605.csv', 'r') as infile:
    reader = csv.reader(infile)
    # to iterate through the rows in the open csv file and check for a match to name
    # add break to prevent next block of code running automatically after match is found
    for row in reader:
        if row[0] == name:
            print("{}: {}".format(row[0], row[1]))
            break

# conditional to input and append csv file if there is no name match
if row[0] != name:
        print("No address found for {}".format(name))
        address = input("Add address: ")

        with open('lab0605.csv', 'a', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow([name, address])