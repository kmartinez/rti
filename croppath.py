#!/usr/bin/env python
# crop off 45 chars of path from the lp file
# redirect output to your new lp file
# there must be a better way buy hey it took minutes to get this far
# note to self comma after print stops extra whitespace being added
# km oct 2016
import sys

linenum = 0
if len(sys.argv) != 2 :
	print "args: filename.lp"
	sys.exit(1)

lines = open(sys.argv[1]).readlines()
for line in lines :
	if linenum == 0 :
		print line,
	else :
		print str(linenum-1) + ".jpg " + line[45::],
	linenum = linenum + 1

