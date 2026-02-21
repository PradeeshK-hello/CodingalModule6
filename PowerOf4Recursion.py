def powerOf4(n):
    if n == 1:
        return "This is a power of 4."
    elif n < 1 or n % 4 != 0:
        return "This is not a power of 4."
    else:
        return powerOf4(n // 4)
n = int(input("Enter a number: "))
print(powerOf4(n))