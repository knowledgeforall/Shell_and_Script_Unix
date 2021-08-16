#!/usr/bin/awk

BEGIN {
    FS=","
}
{
if ($1 == "Name")
    $1=""

if ($2 >=90 && $2 <= 100)
    grade="A"

if ($2 >=80 && $2 <= 89)
    grade="B"

if ($2 >=70 && $2 <= 79)
    grade="C"

if ($2 >=60 && $2 <= 69)
    grade="D"
    
if ($2 >=0 && $2 <= 59)
    grade="E"

printf("%s\t%c\n", $1, grade)

}
END {

}