def incdec(n,num):
    if n<0 or n>num:
        return
    print(n)
    incdec(n-1,num)
    print(n)
n = int(input("Enter any number n: "))
incdec(n,n)