#!/usr/bin/bash

word=word

while [[ $word != "Banana" ]]
do
    echo "Enter another word:"
    read word
done

echo "That's the secret word!"