#!/usr/bin/bash

echo "Is it October?"
read var1
if [[ $var1 = No ]]
then
    echo "Okay."
elif [[ $var1 = Yes ]]
then 
    echo "Then it's time to get spooky!"
else 
    echo "That's not a valid answer."
fi