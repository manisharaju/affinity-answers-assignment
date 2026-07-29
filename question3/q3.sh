#!/bin/sh

if [ $# -ne 1 ]; then
    echo "Usage: $0 <CSV_URL>"
    exit 1
fi

curl -s "$1" |
gawk --csv '
NR > 1 {
    print $8 "|" $2 "|" $5
}
' |
sort -t'|' -k1,1 |
awk -F'|' '
{
    printf "Company Name : %s\n", $2
    printf "Location     : %s\n", $3
    printf "Founded Year : %s\n\n", $1
}
'