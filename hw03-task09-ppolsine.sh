#!/usr/bin/bash

for word in $*
do
    if [[ $word = data ]]
    then
        echo "omelette"
    elif [[ $word = processor ]]
    then
        echo "stir fry"
    elif [[ $word = install ]]
    then
        echo "baked potato"
    elif [[ $word = banana ]]
    then
        echo "burrito"
    fi
done