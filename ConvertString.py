'''
Created on Jul 2, 2021

Name:  Ben Lamb
Program:  ConvertString
Description: Asks user for a word and converts it
to uppercase, replacing t/T's with asterisks
@author: blamb
'''
#Ask user for a sentence
str1 = input("Give me a sentence, any sentence: ")
#Print sentence in all uppercase
print(str1.upper())
#Replace lowercase t's with *
str2 = str1.replace('t', '*')
#Replace uppercase t's with *
str2 = str2.replace('T', '*')
#Print results
print(str2)