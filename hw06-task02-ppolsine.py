#!/usr/bin/python3

# to create the faculty and student lists
Faculty = ["Rucker", "Gatto", "Doheny", "Ingersoll", "Lauer"]
Students = ["Johnson","Russell","Zeck", "Nehdar", "Sainz"]
# prompt for name
name = input("Enter a name: ")
# to match name in students list as true and print expected output
while name in Students:
    print("Hello, Student! The next assignment is Homework 6.")
    name = input("Enter a name: ")
# to match name in students list as true and print expected output
if name in Faculty:
    print("Welcome, Professor {}!".format(name))