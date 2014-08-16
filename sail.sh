#!/bin/sh
case "`wget -qO- https://portal2.community-boating.org/pls/apex/CBI_PROD.FLAG_JS | cut -d '"' -f 2`" in "G") echo "Green" ;; "Y") echo "Yellow" ;; "R") echo "Red" ;; *) echo "Closed" ;; esac
