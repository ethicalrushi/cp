def stepCount(n):
    res = 0
    n = int(n)
    while n > 1:
        if n % 2 == 0:           
            n = n // 2
        elif n==3:
            n = 2
        elif n % 4 == 1: 
            n = n - 1
        else:                      
            n = n + 1
        res += 1
    return res

n= int(input())
print(stepCount(n))