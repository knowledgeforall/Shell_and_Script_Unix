#!/usr/bin/awk

BEGIN {
   FS=","
}
{
if ($2 > 75 && NR > 1)
    print $1
}

END {

}