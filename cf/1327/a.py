t = int(input())

for _ in range(t):
    n, k = [int(x) for x in input().strip().split()]
    nm = n%2
    km = k%2

    if nm==km:
        mn = (k*(1+2*k-1))//2
        if n>=mn:
            res = "YES"
        else:
            res = "NO"
    else:
        res = "NO"

    print(res)