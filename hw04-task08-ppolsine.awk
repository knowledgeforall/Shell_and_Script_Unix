#!/usr/bin/awk

BEGIN { }

!/[0-9].*/ { print $0 }

END { }
