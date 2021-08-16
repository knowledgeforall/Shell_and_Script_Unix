#!/usr/bin/awk

BEGIN {
    FS=","
}
{
total=0

if ($1 =="ADD")
    for (num=2;num<=NF;num++)
        total += $num

if ($1 =="SUB")
    for (num=2;num<=NF;num++)
        total -= $num

print total
}

END {

}