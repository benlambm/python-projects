'''
Created on Jul 15, 2021

Name:  Ben Lamb
Program:  ReadGrades
Description: This program reads grades from text file
and computes min, max, and average
@author: blamb
'''
grades = []

def main():
    print("We are reading in the grade file...")
    fob = open('grades.txt', 'r')
    for line in fob:
        if line == '':
            break
        grades.append(int(line))
    fob.close()
    if not grades:
        print("No grades in this file.")
        quit()
    printList()
    printSorted()
    printMax()
    printMin()
    printAve()
def printList():
    print(grades)
def printSorted():
    grades.sort()
    print(grades)
def printMax():
    print("High score:", max(grades))
def printMin():
    print("Low score:", min(grades))
def printAve():
    sum1 = 0
    for grade in grades:
        sum1 += grade
    avrg = sum1 / len(grades)    
    print("Average score:", avrg)

main()
