'''
Created on Jul 11, 2021

Name:  Ben Lamb
Program:  ReadScores
Description: Reads in player name and golf score from text file
and determines winner based on lowest score
@author: blamb
'''
print('''We are reading in the scores for the Python golf club.
This program determines who won the contest!''')

#create list to temporarily store all golfer scores
scoreBoard = []
#create file handle in read-only
fob = open('golf.txt', 'r')
#read text file line by line
for line in fob:
    golferName = ''
    strScore = ''
    #is next char part of golfer Name or Score?
    for char in line:
        if char.isalpha() or char.isspace():
            #part of Name so add to Name
            golferName += char
        if char.isnumeric():
            #part of Score so add to Score
            strScore += char
    #display one golfer score
    print(golferName.rstrip(), "had a score of", strScore)
    #add this golfer's score to scoreBoard list starting with score
    scoreBoard.append((int(strScore), golferName.rstrip()))
#close file handle
fob.close()
#check if file was empty
if not scoreBoard:
    print("There was no data in the file!!")
    quit()
#determine lowest score
scoreBoard.sort()
#print winner
print("The winning golfer is", scoreBoard[0][1], "with the low score of", scoreBoard[0][0])
