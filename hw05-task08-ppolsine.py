#!/usr/bin/python3

# convert between times
def minhour(sec): 
    sec = sec % (24 * 3600) 
    hr = sec // 3600
    sec %= 3600
    mi = sec // 60
    sec %= 60
    return (hr, mi, sec) 
#prompt for input and display expected outcome
num = int(input("Enter a number of seconds: "))
t = minhour(num) 
print("{} hour, {} minutes, and {} seconds".format(t[0],t[1],t[2]))