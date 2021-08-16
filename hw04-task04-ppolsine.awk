#!/usr/bin/awk

BEGIN {
    FS=","
}
{

if ($3 == "online")
        print $1
}
END {

}