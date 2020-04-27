t = int(input())

for _ in range(t):
    n,a,b,c,d = [int(x) for x in input().strip().split()]
    mn = a-b
    mx = a+b
    if c-d>mx*n or c+d<mn*n:
        print("No")
    else:
        print("Yes")
