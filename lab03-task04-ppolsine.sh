#!/usr/bin/bash

count=1
args=$#
sum=0
while [ $count -le $args ] 
do
    sum=$(($sum + $1))
    count=$((count + 1))
    shift 1
done

echo "$sum"