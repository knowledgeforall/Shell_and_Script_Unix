#!/usr/bin/bash

operator="$1"
shift

count=1
args=$#

if [ "$operator" = "add" ]
then
    sum=0
    while [ $count -le $args ] 
    do
        sum=$(($sum + $1))
        count=$((count + 1))
        shift 1
    done
    echo "$sum"

elif [ "$operator" = "sub" ]
then
    difference=$1
    shift
    while [ $count -lt $args ] 
    do
        difference=$(($difference - $1))
        count=$((count + 1))
        shift 1
    done
    echo `expr $difference`

elif [ "$operator" = "mul" ]
then
    product=1
    while [ $count -le $args ] 
    do
        product=$(($product * $1))
        count=$((count + 1))
        shift 1
    done
    echo $product

elif [ "$operator" = "div" ]
then
    div=$1
    shift
    while [ $count -lt $args ] 
    do
        div=$(($div / $1))
        count=$((count + 1))
        shift 1
    done
    echo `expr $div`

elif [ "$operator" = "exp" ]
then
    base=$1
    shift
    echo $base
    product=1
    while [ $count -lt $args ] 
    do
        product=$(($product * $1))
        count=$((count + 1))
        shift 1
    done
    exp=$(($base ** $product))
    echo $exp

elif [ "$operator" = "mod" ]
then
    mod=$1
    shift
    while [ $count -lt $args ] 
    do
        mod=$(($mod % $1))
        count=$((count + 1))
        shift 1
    done
    echo `expr $mod`
else
    echo "Please select one of the following and try again:"
    echo "add sub mul div exp mod"
fi
