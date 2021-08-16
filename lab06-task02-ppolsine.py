#!/usr/bin/python38

# "mul" function compatible with python 3.8.0
import math
# while true keeps the prompts continuous
while True:
    # to create lists, prompt for input, split the prompts for input to lists, and create operator funtionality
    data = []
    numbers = []
    data = input("Enter calculation: ").split()
    operator = data[0]  
    # to create iteration  to populate the list 'numbers' with data
    for num in data[1:]:
        numbers.append(int(num))
    # to create the math functions according to their operators and print expected output
    def add():
        print(f"Sum: {sum(numbers)}")

    def sub():
        result = numbers[0]
        for num in numbers[1:]:
            result = result - num
        # print at this indentation to prevent printout of every step of subtraction of multiple numbers and only print final difference
        print(f"Difference: {result}")

    def mul():
        # product attribute is python38
        print(f"Product: {math.prod(numbers)}")

    def div():
        result = numbers[0]
        for num in numbers[1:]:
            result = result/num
            print(f"Quotient: {int(result)}")

    def exp():
        base = numbers[0]
        power = numbers[1]
        print(f"Power: {pow(base, power)}")

    def mod():
        result = numbers[0]
        for num in numbers[1:]:
            result = result%num
            print(f"Modulus: {result}")
    # to call the correct functions according to operator input
    if operator == "add":
        add()

    if operator == "sub":
        sub()

    if operator == "mul":
        mul()

    if operator == "div":
        div()

    if operator == "exp":
        exp()

    if operator == "mod":
        mod()