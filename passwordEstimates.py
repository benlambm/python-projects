"""
Created on Jan 31, 2022

Author:  Ben Lamb
Program:  passwordEstimates
Description: A console app that calculates in minutes the time
it would take to crack a password given its length and # of possible characters

"""
secondsPerAttempt = .0001


def main():
    nd = int(input("How many digits long is the passcode? "))
    nc = int(input("How many possible characters are there per digit? "))
    npp = numberPossiblePasswords(nd, nc)
    totalSeconds = maxSecondsToCrack(npp, secondsPerAttempt)
    totalMinutes = totalSeconds / 60
    print("It will take you " + str(totalMinutes) + " minutes maximum to crack the password.")


def numberPossiblePasswords(numDigits, numPossiblePerDigit):
    numPasswords = numPossiblePerDigit ** numDigits
    return numPasswords


def maxSecondsToCrack(numPossiblePasswords, secPerAttempt):
    time = numPossiblePasswords * secPerAttempt
    return time


main()




