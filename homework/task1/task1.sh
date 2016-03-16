cut -d ':' -f1,6 $1 | sed -e 's/^/The home directory of /g' | tr ':' '=' > $2 
