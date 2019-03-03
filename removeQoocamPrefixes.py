#! python3
# remove all Qoocam prefixes from all files in current directory
import os

prefixes = ['KDRaw_', 'Output_', 'Q360_', 'KD3D_']

for fileName in os.listdir():
	for prefix in prefixes:
		newFilename = fileName.replace(prefix, '')
		print(newFilename)
		os.rename(fileName, newFilename)
		fileName = newFilename