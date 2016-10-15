#!/bin/bash

SLEEP=5

if [ -z $1 ]; then
    echo "File name required."
    exit
fi

if [[ ! -f $1 || ! -r $1 || ! -w $1 ]]; then
    echo "Given file either doesn't exist or you lack permissions to write/read it"
    exit
fi

if [ ! -z $2 ]; then
    SLEEP=$2
fi

if [ ! -f "${1}_ORIGINAL" ]; then
    cp $1 "${1}_ORIGINAL"
    echo "Original files has been copied to: ${1}_ORIGINAL"
fi

echo "# # # Simulation has started. Please stop it with CTRL+C once the test is over # # #"

while true; do
    # erease the $1 file so it won't grow forever
    > $1
    while read line; do
        # put new content line by line
        echo $line >> $1
        echo "# Current value: $line"

        sleep $SLEEP
    done < "${1}_ORIGINAL"
done
