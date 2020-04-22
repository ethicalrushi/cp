t = int(input())
for _ in range(t):
    n, q= [int(x) for x in input().strip().split()]
    s=0
    res=0
    for i in range(q):
        u, v = [int(x) for x in input().strip().split()]
        res+=abs(s-u)
        res+=abs(v-u)
        s=v
    
    print(res)