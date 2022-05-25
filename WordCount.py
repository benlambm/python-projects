'''
Created on Jul 2, 2021

Name:  Ben Lamb
Program:  WordCount
Description: Searches a word or phrase for a specific letter
and counts how many times it can be found    
@author: blamb
'''
def main():
    #Ask user for word or phrase
    str1 = input("Please enter a word or phrase: ")
    #Ask user for letter
    char = input("What letter are you looking for (case-sensitive)? ")
    #Call function to count letter
    countLetters(str1, char)
    
def countLetters(word, letter):
    #Count and display total amount of letter in word/phrase
    print(letter, "is found", word.count(letter), "times.")
    
main()