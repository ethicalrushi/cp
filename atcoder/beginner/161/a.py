a,b,c = [int(x) for x in input().strip().split()]

a,b = b,a
a,c = c,a
print(a,b,c)