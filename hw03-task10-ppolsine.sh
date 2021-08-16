#!/usr/bin/bash

words=(pizza cookie steak hungry technology memory error banana)

while true
do
        read -p "Enter a word:"
        response=$(($RANDOM%8))
        random=${words[response]}
        echo $random
        if [[ $random == "cookie" ]]
        then
                echo "Mmmmm.... cookies!"
        fi
done