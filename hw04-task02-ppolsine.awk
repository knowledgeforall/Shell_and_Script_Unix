#!usr/bin/awk
BEGIN { FS="," }
{
if ($3 == "online")
    printf("%s is an online student\n", $1)
if ($3 == "onsite")
    printf("%s is an onsite student\n", $1)
}

END {

}