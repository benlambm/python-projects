'''
Created on Jul 2, 2021

Name:  Ben Lamb
Program:  Words
Description: Asks user for phrase and a letter and 
prints all words that start with that letter
@author: blamb
'''
def main():
    #Ask user to input phrase
    str1 = input("Give me a phrase: ")
    #Ask user to input letter
    char = input("Give me a letter: ")
    #testing print("Counting:", char, "appears in phrase", str1.count(char), "times.")
    #Call function that identifies all words starting with the user-entered letter
    words(str1, char)
    
def words(phrase, ch):
    #Split sentence into list of words
    words = phrase.split(' ');
    #Create list to store matching words
    results = []
    #Examine each word one at a time
    for word in words:
        #does word start with the letter whether uppercase or lowercase?
        if word[0] == ch.lower() or word[0] == ch.upper():
            #if so, add to list
            results.append(word)
    #print list of matching words
    for result in results:
        print(result)
        
main()