'''
Created on Jul 11, 2021
Name:  Ben Lamb
Program:  WriteScores
Description: Lets user input player name and golf score and saves to text file
@author: blamb
'''
print("This program keeps track of the scores for the Python golf club.\n")
input("Press ENTER to begin.")
#create file handle (or new file if needed)
fob = open('golf.txt', 'a')
#does user have another score to enter?
anotherScore = 'yes'
#if so, repeat input
while anotherScore == 'yes':
    #get golfer's name
    name = input("Golfer's name: ")
    #get golfer's score
    score = input("Golfer's score: ")
    #save name and score to txt file
    fob.write(f"{name} {score} \n")
    #does user have another score to enter?
    anotherScore = input("More golfers? (yes/no)")
#close file handle
fob.close()