#!/usr/bin/awk

BEGIN {
    FS=","
}
{
if ($3 == "online")
    online++

if ($3 == "onsite")
    onsite++
}
END {
printf("online %d\n", online)
printf("onsite %d\n", onsite)
}