t = int(input())
s = "abcdefghijklmnopqrstuvwxyz"
for _ in range(t):
    n,a,b = [int(x) for x in input().strip().split()]
    curr = s[:b]
    res = curr*((n//b+1)*b)
    res = res[:n]
    print(res)

    
