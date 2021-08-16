#!/usr/bin/bash

echo "Enter your name:"
read name

echo "Enter the date:"
read date

echo "Enter your city:"
read city

echo "Enter the current temperature:"
read temperature

echo "Enter todays's birthday:"
read birthday

echo "Enter your payable bills:"
read bills

echo "Good day, $name.  Today is $date in the city of $city.  It is a beautiful $(date +"%A"), the temperature is $temperature degrees.  Today is $birthday's birthday.  Insurance is payable, as are the water, gas, and light bills for a total of $ $bills."