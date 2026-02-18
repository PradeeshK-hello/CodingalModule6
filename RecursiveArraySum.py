def arr_sum(a):
    length = len(a)
    if length == 1:
        return a[0]
    return a[0] + arr_sum(a[1:])
a = [1,2,3,4,5,6,7,8,9,10]
print("The sum of array elements is:",arr_sum(a))