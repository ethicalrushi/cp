t = int(input())

for _ in range(t):
    a, b = [int(x) for x in input().strip().split()]
    rem = a%b
    if a<b:
        res = b-a
    else:
        res = (b-rem)%b
    print(res)