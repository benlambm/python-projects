'''
Created on Jun 17, 2021

Name:  Ben Lamb
Program:  BaseballSeating
Description: This self-serve ticket kiosk program enables
a customer to purchase stadium seating and calculates the total
(subtracting a 10% discount if the total is over $300)
@author: blamb
'''
#Constants for menu choices
PURCHASE_LOWER = 1
PURCHASE_UPPER = 2
PURCHASE_BLEACHER = 3
PRINT_ALL = 4
CALC_TOTAL = 5
QUIT_CHOICE = 6

def main():
    choice = 0
    costLower = 0
    costUpper = 0
    costBleacher = 0
    
    while choice != QUIT_CHOICE:
        displayMenu()
        choice = int(input("Enter your choice: "))
        if choice == PURCHASE_LOWER:
            costLower = purchaseLower()
        elif choice == PURCHASE_UPPER:
            costUpper = purchaseUpper();
        elif choice == PURCHASE_BLEACHER:
            costBleacher = purchaseBleachers()
        elif choice == PRINT_ALL:    
            printIt(costLower, costUpper, costBleacher)
        elif choice == CALC_TOTAL: 
            calcTotal(costLower, costUpper, costBleacher)  
        elif choice == QUIT_CHOICE:
            print('Exiting the program...')
        else:
            print('Error: invalid selection.')

def displayMenu():
    print('        MENU')
    print('1) Purchase reserved lower tickets')
    print('2) Purchase reserved upper tickets')
    print('3) Purchase bleacher seats')
    print('4) Print information')
    print('5) Calculate total')
    print('6) Quit')

def purchaseLower():
    COST_EACH = 60.00
    quantity = int(input("How many reserved lower stadium tickets ($60.00 each)? "))
    print("The total cost of {:.2f} seat(s) at ${:.2f} is ${:.2f}".format(quantity, COST_EACH, quantity * COST_EACH))
    return quantity * COST_EACH
def purchaseUpper():
    COST_EACH = 45.00
    quantity = int(input("How many reserved upper stadium tickets ($45.00 each)? "))
    print("The total cost of {:.2f} seat(s) at ${:.2f} is ${:.2f}".format(quantity, COST_EACH, quantity * COST_EACH))
    return quantity * COST_EACH
def purchaseBleachers():
    COST_EACH = 20.00
    quantity = int(input("How many bleacher seat tickets ($20.00 each)? "))
    print("The total cost of {:.2f} seat(s) at ${:.2f} is ${:.2f}".format(quantity, COST_EACH, quantity * COST_EACH))
    return quantity * COST_EACH
def printIt(costL, costU, costB):
    print("""
Cost reserved lower tickets: ${:.2f}
Cost reserved upper tickets: ${:.2f}
Cost bleacher seat tickets: ${:.2f}
        """.format(costL, costU, costB)) 

def calcTotal(costL, costU, costB): 
    if costL + costU + costB > 300:
        calcDiscount(costL, costU, costB)
    else:
        print("The total cost of your order is ${:.2f}".format(costL + costU + costB))

def calcDiscount(l, u, b):
    print("Since your total is over $300, you get 10% off today!")
    total = l + u + b
    discount = total / 10
    print("Your discount is ${:.2f} for a net cost of ${:.2f}".format(discount, total-discount))
    
main()