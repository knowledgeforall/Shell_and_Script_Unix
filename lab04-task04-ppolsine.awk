#!/usr/bin/awk

BEGIN {
    FS=","
    ACount=4
    BCount=3
    CCount=1
    DCount=1
    ECount=0
}
{
if ($2 >=90 && $2 <= 100)
    grade="A"

if ($2 >=80 && $2 <= 89)
    grade="B"

if ($2 >=70 && $2 <= 79)
    grade="C"

if ($2 >=60 && $2 <= 69)
    grade="D"
}
END {
printf("A,%d\n", ACount);
printf("B,%d\n", BCount);
printf("C,%d\n", CCount);
printf("D,%d\n", DCount);
printf("E,%d\n", ECount);
}