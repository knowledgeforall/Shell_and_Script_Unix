#!/usr/bin/awk

BEGIN{
    FS=","
}
{
if (NF <= 4)
    print NR
}
END{

}