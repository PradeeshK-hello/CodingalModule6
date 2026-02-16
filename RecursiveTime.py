def fac(n1):
    if(n1==1 or n1==0):
        return 1
    return n1*fac(n1-1)
print("Time Complexity for first code: O(n)")
def print1to10(n2):
    if(n2>10):
        return
    print(n2)
    print1to10(n2+1)
print("Time Complexity for second code: O(n)")