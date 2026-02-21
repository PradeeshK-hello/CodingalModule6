def powerOf2(n):
    if n == 1:
        return "This is a power of 2."
    elif n < 1 or n % 2 != 0:
        return "This is not a power of 2."
    else:
        return powerOf2(n // 2)
n = int(input("Enter a number: "))
print(powerOf2(n))