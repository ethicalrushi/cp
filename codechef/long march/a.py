t = int(input())

for _ in range(t):

    n, f = [int(x) for x in input().strip().split()]
    a = [int(x) for x in input().strip().split()]
    b = [int(x) for x in input().strip().split()]
    c = [10**10 for i in range(f)]

    for i in range(n):
        if c[a[i]-1] == 10**10:
            c[a[i]-1] = b[i]
        else:
            c[a[i]-1]+=b[i]
    
    print(min(c))