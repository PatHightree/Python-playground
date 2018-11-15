#! python3
# parse the files in the removeOutputs directory, for each file move the source file from the sources directory to the removeOutputs directory
sources = 'C:\\Users\\patri\\Pictures\\Qoocam capture'
removeOutputs = sources + '\\KDOutput\\Remove'

import os
import shutil

os.chdir(sources)
for removeOutput in os.listdir(removeOutputs):
	removeSource = removeOutput. replace('Output_', '')
	print ('Searching for ' + removeSource)
	for source in os.listdir(sources):
		if source.lower() == removeSource.lower():
			print ('Found ' + source)
			shutil.move(os.path.join(sources, source), removeOutputs)

# for folderName, subFolders, fileNames in os.walk('C:\\Users\\patri\\Pictures\\2018-11-12\\KDOutput')
# for folderName, subFolders, fileNames in os.walk('C:\\Users\\patri\\Pictures'):
# 	print (folderName)