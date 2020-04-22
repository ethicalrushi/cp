t = int(input())
for _ in range(t):
    x, y, a, b = [int(x) for x in input().strip().split()]

    res = -1
    if(y-x)%(a+b)==0:
        res = (y-x)//(a+b)
    print(res)
