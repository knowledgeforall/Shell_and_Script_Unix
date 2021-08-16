BEGIN {
    FS=","
    online=0
    onsite=0
    count_online=0
    count_onsite=0
    highest=1
    lowest=1000
}
{
if($1 == "Name")
  next

if($3 == "online")
{
    online+=($2)
    count_online+=1
    online_scores[count_online] = $2
}

if($3 == "onsite")
{
    onsite+=($2)
    count_onsite+=1
    onsite_scores[count_onsite] = $2
}

if($2 > highest)
    highest=$2

if($2 < lowest)
    lowest=$2

if(idxOnline%2)
  medianOnline = online_scores[(idxOnline+1)/2]
else
  medianOnline = online_scores[(idxonline/2)]

if(idxOnsite%2)
  medianOnsite = onsite_scores[(idxOnsite+1)/2]
else
  medianOnsite = onsite_scores[(idxOnsite/2)]

}

END {
    print "Section Average";
    printf "%s %.2f %.2f\n","online", (online/count_online), medianOnline
    printf "%s %.2f %.2f\n","onsite", (onsite/count_onsite), medianOnsite
    print "Highest grade : "highest
    print "Lowest grade : "lowest
}
