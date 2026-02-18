def arr_greatest(a):
    length = len(a)
    if length == 1:
        return a[0]
    return max(a[0],arr_greatest(a[1:]))
a=[1,4,100,6,23]
print("The largest number in the given array is:",arr_greatest(a))