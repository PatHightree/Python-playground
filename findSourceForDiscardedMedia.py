#! python3
# Specify the folder of the Qoocam source media and the root folder of the processed media.
# This program will list the source media for which no processed media exists.

sourceFolder = 'D:\\'
processedRootFolder = 'C:\\Users\\patri\\Pictures'

import os

def CollectSources():
	sources = []
	for folderName, subFolders, fileNames in os.walk(sourceFolder):
		sources += fileNames
	return [s.lower() for s in sources]

def CollectQoocamMedia():
	media = []
	for folderName, subFolders, fileNames in os.walk(processedRootFolder):
		media += fileNames
	# Remove all files from list which do not start with Output_
	qoocamMedia = [ medium for medium in media if medium.startswith('Output_')]
	return [s.lower() for s in qoocamMedia]

def FindOrphans(sources, qoocamMedia):
	orphans = sources
	for sourceFile in sources:
		processedFile = 'Output_' + sourceFile
		if (processedFile.lower() in qoocamMedia):
			orphans.remove(sourceFile)
			continue
	return orphans

sources = CollectSources()
# print(sources)
print(str(len(sources)), 'sources found in', sourceFolder)
qoocamMedia = CollectQoocamMedia()
print(str(len(qoocamMedia)), 'Qoocam Output_ files found in', processedRootFolder)
# print(qoocamMedia)

orphans = FindOrphans(sources, qoocamMedia)
print(str(len(orphans)), 'orphans found')