#!/usr/bin/env python
# tool to rename all images in a dir sequentially 0.jpg to n.jpg
# used so that random incoming names conform to to a numbered list
# so ptm fitter is happier (and matches names in .lp file)
# Kirk Martinez Jan 2017
import os
import sys
import glob

if len(sys.argv) != 2 :
	print "args: pictures- directory"
	sys.exit(1)

#get a list of files
# nikons tend to make DSC_6082.JPG
print "looking at dir: " + sys.argv[1]
# assume if there is a file 0.jpg that its all OK
if os.path.isfile(sys.argv[1] + "/0.jpg") :
	print "already OK with files named 0.jpg 1.jpg.."
	sys.exit(1)

# flag to say we need to convert the folder
needsconversion = 0

filelist = glob.glob(sys.argv[1] + '/*.JPG')
if len(filelist) != 0:
	print "its a .JPG picture folder"
	needsconversion = 1
else:
	# check if its an incoming .jpg
	filelist = glob.glob(sys.argv[1] + '/*.jpg')
	if len(filelist) != 0:
		print "its a .jpg picture folder"
		needsconversion = 1

if needsconversion == 1:
	N = 0
	for filen in filelist :
		newname = sys.argv[1] + "/" + str(N) + ".jpg"
		#print filen + " to " + newname
		os.rename(filen, newname)
		N = N + 1
	print "renamed to 0.jpg.."
else:
	print "please check dir as I could not find images"
