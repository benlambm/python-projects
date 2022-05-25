'''

Name:  Ben Lamb
Program:  DisneyMenu
Description: This is the ticket kiosk UI for a
Disney theme park that enables user to purchase
admission, parking, food/drink, and mickey mouse 
souvenir and print totals

'''

# Constants for the menu choices
PURCHASE_ADULT = 1
PURCHASE_CHILD = 2
PURCHASE_MOUSE_EARS = 3
PURCHASE_PARKING = 4
PURCHASE_FOOD = 5
PRINT_ALL = 6
CALC_TOTAL = 7
QUIT_CHOICE = 8

# The main function.
def main():
    # The choice variable controls the loop
    # and holds the user's menu choice.
    choice = 0
    costAdult=0
    costKid=0
    costEars=0
    costPark=0
    costFood = 0

    while choice != QUIT_CHOICE:
        
        # display the menu.
        display_menu()

        # Get the user's choice.
        choice = int(input('Enter your choice: '))

        # Perform the selected action.
        if choice == PURCHASE_ADULT:
            costAdult = purchaseAdult()
        elif choice == PURCHASE_CHILD:
            costKid = purchaseKid()
        elif choice == PURCHASE_MOUSE_EARS:
            costEars = purchaseEars()
        elif choice == PURCHASE_PARKING:
            costPark = purchaseParking();
        elif choice == PURCHASE_FOOD:
            costFood = purchaseFood()
        elif choice == PRINT_ALL:    
            printIt(costAdult,costKid,costEars,costPark,costFood)
        elif choice == CALC_TOTAL: 
            calcTotal(costAdult,costKid,costEars,costPark,costFood)  
        elif choice == QUIT_CHOICE:
            print('Exiting the program...')
        else:
            print('Error: invalid selection.')
    
# The display_menu function displays a menu.
def display_menu():
    print('        MENU')
    print('1) Purchase adult tickets')
    print('2) Purchase child tickets')
    print('3) Purchase cool mouse ears')
    print('4) Purchase parking')
    print('5) Purchase food')
    print('6) Print information')
    print('7) Calculate total')
    print('8) Quit')


#purchaseAdult() method returns how much the adult tickets will cost
def purchaseAdult():
    COST_EACH = 95.00
    quantity = int(input("How many adult tickets ($95.00 each)? "))
    return quantity * COST_EACH

#purhcaseKid() function returns how much the kids tickets will cost
def purchaseKid():
    COST_KID = 65.00
    quantity = int(input("How many kid tickets ($65.00 each)? "))
    return quantity * COST_KID

#purhcaseKid() function returns how much the kids tickets will cost
def purchaseEars():
    EAR_COST = 9.00
    quantity = int(input("How many Mickey Mouse ears ($9.00 each)? "))
    return quantity * EAR_COST

# purchaseParking() just returns 25 for parking    
def purchaseParking():
    COST_PARKING = 25
    print("Parking costs $25.00")
    return COST_PARKING

# purchaseFood() asks for the number of hot dogs and sodas, calculates the total cost
# and returns this value   
def purchaseFood():
    COST_DOGS = 12
    COST_SODA = 6
    print("We have hot dogs ($12.00 each) and soda ($6.00 each) only")
    quantityDogs = int(input("How many hot dogs? "))
    quantitySodas = int(input("How many drinks? "))
    return quantityDogs * COST_DOGS + quantitySodas * COST_SODA
   
#printIt() prints our each individual cost (see sample output
def printIt(costA, costK, costE, costP, costF):
    print("""
Cost adults tickets: ${:.2f}
Cost kids tickets: ${:.2f}
Cost mouse ears tickets: ${:.2f}
Cost parking: ${:.2f}
Cost food: ${:.2f}
        """.format(costA, costK, costE, costP, costF))
   
#calcTotal() calculates and prints the total cost    
def calcTotal(costA, costK, costE, costP, costF):
    print("The total cost of your order is ${:.2f}".format(costA +costK + costE + costP + costF))
    
# Call the main function.
main()