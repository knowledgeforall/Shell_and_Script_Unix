#!/usr/bin/awk

BEGIN {
    FS=","
    salecount = 0
}
{
  if($1 == "Name")
    next

  if($3 == "")
    saleamt=0
  else
    saleamt=$3
  totalsales=totalsales+saleamt
  salecount++
}

END {
print "AVG: " totalsales/salecount
}
