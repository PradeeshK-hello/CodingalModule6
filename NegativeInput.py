def negativeInput(n):
    n = int(input("Enter a number: "))
    while n >= 0:
        negativeInput(n)
    else:
        print("Negative number entered. Exiting the program.")
negativeInput(0)