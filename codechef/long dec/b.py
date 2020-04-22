t = int(input())
for _ in range(t):
    n = int(input())
    arr= [int(x) for x in input().strip().split()]
    zc=0
    tc=0
    for a in arr:
        if a==0:
            zc+=1
        if a==2:
            tc+=1
    
    res = zc*(zc-1)//2+tc*(tc-1)//2
    print(res)