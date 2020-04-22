n, m = [int(x) for x in input().strip().split()]
a = [int(x) for x in input().strip().split()]

a.sort(reverse=True)
s = sum(a)
thresh = s/(4*m)
flag=True
for i in range(m):
    if a[i]< thresh:
        flag=False
        break

if flag:
    print("Yes")
else:
    print("No")