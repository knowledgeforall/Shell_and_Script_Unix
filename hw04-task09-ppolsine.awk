#!/usr/bin/awk

BEGIN {
    FS=","
}
{
saleamt=$3
totalsales=totalsales+saleamt
}
END {
print totalsales
}