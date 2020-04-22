a = [int(x) for x in input().strip().split()]
b = [int(x) for x in input().strip().split()]
c = [int(x) for x in input().strip().split()]

a.sort()
b.sort()
c.sort()

d = [a[1],b[1],c[1]]
d.sort()
print(d[1])