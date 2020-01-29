#!/bin/bash
input="in.txt"
while IFS= read -r line; do
  python3 gameMaster.py <<< "$line"
  # <<<"Q"
done < "$input"

# while read line; do
#     VALUE=$line   ## No spaces allowed
#     python3 gameMaster.py 
#     "$line"
#       ## Quote properly to isolate arguments well
#     echo "$VALUE+huh"  ## You don't expand without $
# done < "in.txt"