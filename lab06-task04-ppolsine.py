#!/usr/bin/python3

# to import a module for reading and writing csv files
import  csv
# to create a function that classifies number grades to letter grades
def letter_grade(grade):
    if grade>=97 and grade<=100:
        return "A+"
    if grade >= 93 and grade <= 96:
        return "A"
    if grade >= 90 and grade <= 92:
        return "A-"
    if grade >= 87 and grade <= 89:
        return "B+"
    if grade >= 83 and grade <= 86:
        return "B"
    if grade >= 80 and grade <= 82:
        return "B-"
    if grade >= 77 and grade <= 79:
        return "C+"
    if grade >= 73 and grade <= 76:
        return "C"
    if grade >= 70 and grade <= 72:
        return "C-"
    if grade >= 67 and grade <= 69:
        return "D+"
    if grade >= 63 and grade <= 66:
        return "D"
    if grade >= 60 and grade <= 62:
        return "D-"
    if grade >= 0 and grade <= 59:
        return "E"
# to create a list to output to txt file
output_list=[["Name","grade","letter"]]
# to use the csv module to open and read the input file
with open("lab0605.csv","r") as infile:
    reader = csv.reader(infile)
# to set a condition and iterate through and populate the output list
    i = 1
    for row in reader:
        if i != 1:
            name = row[0]
            grades = row[1::]
            sum = 0
            for grade in grades:
                sum = sum+int(grade)
            average = float(sum/len(grades))
            average = "{:.2f}".format(average)
            letter = letter_grade(float(average))
            output_list.append([name,average,letter])
        i = 0
    # to write the expected output to the output file
    with open("out604.txt)", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(output_list)
    # to close the open file
    file.close()