'''
Created on Jul 11, 2021

Name:  Ben Lamb
Program:  EmailAddresses
Description: Reads file for and counts email addresses
by type
@author: blamb
'''
#create file handle
fob = open('emails.txt', 'r')
#create email-type counters
gmail = 0
vccs = 0
other = 0
#for each line of text file...
for email in fob:
    #is it a gmail address?
    if 'gmail.com' in email:
        gmail += 1
    #is it a vccs address?
    elif 'email.vccs.edu' in email:
        vccs += 1
    #is it an other address?
    else:
        other += 1
#Display counter results
print(f"The file had {vccs} occurrences of email.vccs.edu")
print(f"The file had {gmail} occurrences of gmail.com")
print(f"There were {other} other addresses in the file.")
#close file handle
fob.close()       