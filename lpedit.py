#!/usr/bin/env python3
# crop off image name and path from the lp file
# replace by incrementing name like 000.jpg 001.jpg...
# redirect output to your new lp file
# there must be a better way buy hey it took minutes to get this far

# km oct 2016
import sys

linenum = 0
if len(sys.argv) != 2 :
    print("args: filename.lp")
    sys.exit(1)

lines = open(sys.argv[1]).readlines()
for line in lines :
    if linenum == 0 :
    # its the top number - keep it
    # end in print stops it adding a crlf as its already in last string
        print(line, end="")
    else :
        fields = line.split(" ")
        print(f'{linenum-1:03d}' + ".jpg " + fields[1] + " " + fields[2] + " " + fields[3], end="")
    linenum = linenum + 1

