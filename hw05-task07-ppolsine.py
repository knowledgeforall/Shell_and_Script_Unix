#!/usr/bin/python3

#prompt for required data and split
data = input("Please enter your name, occupation, birth month, birth state, interests, relative: ")
dataList = data.split(", ")
#insert and display split data in text
print(f"My name is {dataList[0]}. "
      f"I am a fiercely loyal {dataList[1]}."
      f" You might think I’m crazy, but I was born in {dataList[3]} so I can’t help it."
      f" I like {dataList[4]}, but I love my {dataList[5]}. And yes, they bought me this shirt."
      f" I was born in {dataList[2]}.")