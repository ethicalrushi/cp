n = int(input())

arr = [int(x) for x in input().strip().split()]

mx = 0

res = []
s=0
for a in arr:
    s = mx+a
    res.append(s)
    mx = max(mx, res[-1])

print(*res)
