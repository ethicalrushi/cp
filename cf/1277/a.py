import math
t = int(input())
for _ in range(t):
    n = int(input())
    dig = int(math.log10(n))+1
    mn = int(str(n)[0])
    
    res = 9*(dig-1)+mn-1
    if int(str(mn)*dig)<=n:
        res+=1
    print(res)