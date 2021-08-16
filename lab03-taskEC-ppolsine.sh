#!/usr/bin/bash

pluralverbs=(eats swims fights shaves dances flies laughs works codes gambles)
adjs=(random muscular colorful fanciful deranged hysterical funky nervous sexy contagious)
pluralnouns=(porpoises T-Rexes jackalopes unicorns octopuses tarantulas aliens worms giraffes penguins)
adverbs=(quickly early slowly thoughtfully scientifically randomly weirdly sternly gently freakishly)
gerunds=(jogging playing composing staring chewing painting parasailing carving skiing bowling)
place=(Atlantis Casablanca Wakanda Narnia Antartica Albuquerque Timbuktu Podunk Olympus Mongolia)
count=0

echo "Here are three of ten million possible auto generated tasks to complete using Bash:"
echo ""

while [ $count -le 2 ]
do
    response=$(($RANDOM%10))
    random1=${pluralverbs[response]}
    random2=${adjs[response]}
    random3=${pluralnouns[response]}
    random4=${adverbs[response]}
    random5=${gerunds[response]}
    random6=${place[response]}
    echo "Write a bash script that $random1 with $random2 $random3 $random4 while $random5 in $random6"
    echo ""
    count=$((count + 1))
done