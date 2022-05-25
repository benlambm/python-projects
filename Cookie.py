'''
Created on Jul 22, 2021

Name:  Ben Lamb
Program:  Cookie
Description: A cookie calculator that takes a cookie-cutter (OOP) approach
to adding up the number of packages of cookies you wish to buy and the
total cost (10% off if over $30 for any cookie type)
@author: blamb
'''
class Cookie:
    def __init__(self, name, number, costEach):
        self.name = name
        self.number = number
        self.costEach = costEach
    def addPackages(self, num):
        self.number += num
    def toString(self):
        print(f"There are {self.number} packages of {self.name} cookies and each package costs $"
               + format(self.costEach, ',.2f')) 
        print("\tfor a total cost of $", format(self.totalCost(self.number, self.costEach), 
                '.2f'), "and a net cost of $", format(self.net(self.number, self.costEach), '.2f'))
    def totalCost(self, num, cost):
        return num * cost
    def discount(self, num, cost):
        if num * cost >= 30:
            return num * cost * .1
        return 0
    def net(self, num, costEach):
        return (num * costEach) - self.discount(num, costEach)
    
def main():
    moreCookies = "yes"
    subtotals = []
    while moreCookies == "yes":
        name = input("What type of cookie? ")
        number = int(input("How many packages are there? "))
        cost = float(input("How much does each cost? "))
        cookie = Cookie(name, number, cost)
        cookie.toString()
        morePackages = input("Should we add more boxes of this type? (yes or no): ")
        while morePackages == "yes":
            increaseBy = int(input("How many more boxes of this type should be added? "))
            cookie.addPackages(increaseBy)
            cookie.toString()
            morePackages = input("Should we add more boxes of this type? (yes or no): ")       
        subtotals.append(cookie.net(cookie.number, cookie.costEach))
        moreCookies = input("More cookies to register? (yes or no)")
        num_of_types = len(subtotals)
        total = 0
        for sub in subtotals:
            total += sub
    print(f"There were {num_of_types} different cookie types and the total amount for all of the cookies was $", 
          format(total, '.2f'))
    
main()