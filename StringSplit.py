'''
Created on Jul 2, 2021

Name:  Ben Lamb
Program:  StringSplit
Description: Asks user for a date and converts it
to standard 'American' format
@author: blamb
'''
import datetime
#Get user's date and transform it
def main():
    #save user's date
    user_date = input("Enter a data as MM/DD/YYYY (e.g. 7/12/2021): ")
    #call function to decompose it
    dates = splitDate(user_date)
    #turn it into a datetime Object for easier shorthand formatting
    userDateObject = datetime.datetime(dates[2], dates[0], dates[1])
    #call function to format and display date
    getMonth(userDateObject)
    
# Accepts one string, returns three strings: Day, Month, and Year
def splitDate(str1):
    #split up date by / and store in list
    date_bits = str1.split('/')
    #return values are month, day, and year
    return (int(date_bits[0]), int(date_bits[1]), int(date_bits[2]))

# Accepts the one or two digit month and returns the three letter name
def getMonth(dateX):
    #print using datetime formating method
    print(dateX.strftime("%b"), str(dateX.day) + ",", dateX.year)
    
main()