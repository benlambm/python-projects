'''
Created on Jun 17, 2021

Name:  Ben Lamb
Program:  ColorFunction
Description: This program asks user for names of two
primary colors and outputs their secondary color
@author: blamb
'''
def main():
    #ask user for two primary colors
    colorA = input("Enter the first primary color (small letters): ")
    colorB = input("Enter the second primary color (small letters): ")
    resultingColor = mixColors(colorA, colorB)
    printValue(resultingColor)
    
def mixColors(color1, color2):    
    #validate that user chose two different colors
    if color1 == color2: print("You need to enter two different primary colors."); exit()
    
    #validate user chose primary colors
    if color1 != "red" and color1 != "blue" and color1 != "yellow" \
    or color2 != "red" and color2 != "blue" and color2 != "yellow":
        print("You did not enter two primary colors."); exit()
    
    #what is first primary color    
    if color1 == "red":
        #since first color is red, what is second color?
        if color2 == "blue": return "purple"
        if color2 == "yellow": return "orange"
    elif color1 == "blue":
        #since first color is blue, what is second color?
        if color2 == "red": return "purple"
        if color2 == "yellow": return "green"
    else:
        #since first color is yellow, what is third color?
        if color2 == "red": return "orange"
        if color2 == "blue": return "green"
             
def printValue(result):
    print("You will get", result)
main()  