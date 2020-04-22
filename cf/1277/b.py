import bisect
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    dic = {}
    b = []
    for a in arr:
        if a%2==0 and a not in dic:
            dic[a]=1
            b.append(a)

    b.sort()
    l = len(b)
    res=0
    for i in range(l-1,-1,-1):
        temp = b[i]
        dic[temp] = 0
        while temp%2==0 and (temp not in dic or dic[temp]==0):
            temp = temp//2
            res+=1
    
    print(res)
        

