'''
Created on Jul 15, 2021

Name:  Ben Lamb
Program:  WSWinners
Description: This program asks user for a baseball team name
and checks how many times they won the World Series
@author: blamb
'''
def main():
    winners = readWinners()
    while 0 == 0:
        teamName = input("Enter the name of a team: (Type DONE to end) \n")
        if teamName == "DONE":
            quit()
        if teamName in winners:
            wins = 0;
            for team in winners:
                if team == teamName:
                    wins += 1
            print(f"The {teamName} won the World Series {wins} time(s) between 1903 and 2020.")
        else:
            print(f"The {teamName} never won the World Series...")

def readWinners():
    infile = open('WorldSeriesWinners.txt', 'r')
    # Read the contents of the file into a list.
    winners = infile.readlines()
    # Close the file.
    infile.close()
    # Strip the \n from each element.
    index = 0
    while index < len(winners):
        winners[index] = winners[index].rstrip('\n')
        index += 1
    # print(winners)
    return winners
main()