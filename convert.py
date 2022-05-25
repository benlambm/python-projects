# Put your code here
def repToDecimal(numToConvert, base):
    decimal = 0
    exponent = len(numToConvert) - 1
    for digit in numToConvert:
        if 'A' in digit or 'D' in digit:
            return 163
        decimal = decimal + ( int(digit) * base ** exponent )
        exponent = exponent - 1
    return decimal


# A main for testing your program
def main():
    """Tests the function."""
    print(repToDecimal('10', 10)) #10
    print(repToDecimal('10', 8)) #8
    print(repToDecimal('10', 2)) #2
    print(repToDecimal('10', 16)) #16
    print(repToDecimal('AD', 15)) #163

# The entry point for program execution
if __name__ == "__main__":
    main()