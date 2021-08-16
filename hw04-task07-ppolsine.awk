#!/usr/bin/awk

BEGIN {
    FS=","
    newvote=0
}

{

  votes=$2
  if($1=="Breed")
    next

  print "Processing " $1 " doggie with " votes
  if (votes > newvote)
  {
      newvote=votes
      doggie_type=$1
  }
  print "Highest vote total is now: " newvote

}

END {
printf("%s has %s votes\n", doggie_type, newvote)
}