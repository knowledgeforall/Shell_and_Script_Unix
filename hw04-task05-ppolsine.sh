#!/bin/bash

#specify the delimiter as ","
awk -F, '

/./ {
#initialize the total variable as 0
total=0

#loop all the intergers delimited by commas and add it to the
#variable total
#Here NF represents number of fields present in a record

for(i=1; i<=NF; i++)
total += $i

#post adding all the integers, print to console
print total
}' $1