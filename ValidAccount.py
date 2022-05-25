'''
Created on Jul 15, 2021

Name:  Ben Lamb
Program:  ValidAccount
Description: This program checks user input against list to
see if they have a legitimate account number
@author: blamb
'''
def main():
    accounts = readAccounts()
    while 0 == 0:
        acctNum = input("Enter the seven-digit account number to be validated: Or Enter -999 to end program\n")
        if int(acctNum) == -999:
            quit()
        if acctNum in accounts:
            print(f"Account number {acctNum} is valid.")
        else:
            print(f"Account number {acctNum} is not valid.")

def readAccounts():
    infile = open('charge_accounts.txt', 'r')
    # Read the contents of the file into a list.
    accounts = infile.readlines()
    # Close the file.
    infile.close()
    # Strip the \n from each element.
    index = 0
    while index < len(accounts):
        accounts[index] = accounts[index].rstrip('\n')
        index += 1
    return accounts
main()