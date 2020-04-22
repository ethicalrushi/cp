n, m = [int(x) for x in input().strip().split()]
a = [int(x) for x in input().strip().split()]

s = sum(a)
if s>n:
    print(-1)
else:
    print(n-s)