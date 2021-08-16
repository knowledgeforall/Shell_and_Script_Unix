#!/usr/bin/bash

echo "Please select one of the following:"
echo "add sub mul div exp mod"

echo "Enter the operator:"
read operator

if [[ $operator = add ]]
then
    opr="+"
elif [[ $operator = sub ]]
then
    opr="-"
elif [[ $operator = mul ]]
then
    opr="*"
elif [[ $operator = div ]]
then
    opr="/"
elif [[ $operator = exp ]]
then
    opr="**"
elif [[ $operator = mod ]]
then
    opr="%"
fi

echo "Enter the first number:"
read num1

echo "Enter the second number"
read num2

echo "The $operator of $num1 and $num2 is $(( $num1 $opr $num2 ))"