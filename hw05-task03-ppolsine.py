#!/usr/bin/python3
#creating array and setting count
names = [] 
count=0
#populating array
while count<10:
name = input('Enter a name : ')
count=count+1
names.append(name)
#sorting and displaying expected output
if names:
names.sort()
print(names)