'''
Created on Jul 2, 2021

Name:  Ben Lamb
Program:  VowelsAndConsonants
Description: Counts number of vowels and consonants
in a user's word or sentence
Documentation Note: I define 'y' as a consonant
@author: blamb
'''
#Asks the user for input and accepts it as a string. 
def main():
    sentence = input("Give me a string to analyze: ")
    #Call function that counts vowels and consonants in string
    count(sentence)
    
#Accepts any string and prints number of consonants and vowels
def count(strX):
    #create integer to store total number of vowels
    vowels = 0;
    #create integer to store total number of consonants
    consonants = 0;
    #examine each character in given string one at a time
    for char in strX:
        #Is this character a vowel (and not a space)?
        if char=='a' or char=='A' \
        or char=='e' or char=='E' \
        or char=='i' or char=='I' \
        or char=='o' or char=='O' \
        or char=='u' or char=='U' and not char.isspace():
            #if so, increment number of vowels by one
            vowels += 1
        #Is this character a consonant (and not a space)?
        elif (not char.isspace() and char.isalpha()):
            #if so, increment number of consonants by one
            consonants += 1
    #Display totals back to user
    print(f"There are {vowels} vowels and {consonants} consonants.")
    
main()