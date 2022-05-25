'''
Created on Sept 9, 2021

Name:  Ben Lamb
Program:  modify_benlamb
Description: A search-and-replace script for the command line
@author: blamb
'''
import sys

#read in command-line args
fileSpec = sys.argv[1]
searchText = sys.argv[2]
replaceText = sys.argv[3]

#open script with target text
inFile = open(fileSpec, 'r')
script_contents = inFile.read()
inFile.close()

#search for and replace target text
fill = script_contents.replace(searchText, replaceText)
print("Update complete! Saving file...")

#write update to file
outPointer = open(fileSpec,'w')
outPointer.write(fill)
outPointer.close()