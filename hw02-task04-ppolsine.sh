echo "$(<hw0204.txt)" | tr " " "\n" | sort | uniq -i | wc -w