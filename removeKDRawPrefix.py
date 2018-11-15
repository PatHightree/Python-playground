#! python3
# remove KDRaw_ prefix from all files in current directory
import os

prefix = 'KDRaw_'

for fileName in os.listdir():
	if fileName.startswith(prefix):
		newFilename = fileName.replace(prefix, '')
		print(newFilename)
		os.rename(file, newFilename)