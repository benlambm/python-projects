
import math


def main():
    while True:
        # Receive the input number from the user
        user_input = input("Enter a positive number of press Enter/return to quit: ")
        if not user_input.isnumeric():
            quit()
        x = float(user_input)

        newton(x)

        # Output the result
        print("The program's estimate is", estimate)
        print("Python's estimate is", math.sqrt(x))

def newton(x):
    # Initialize the tolerance and estimate
    tolerance = 0.000001
    global estimate
    estimate = 1.0
    # Perform the successive approximations
    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            break

main()
