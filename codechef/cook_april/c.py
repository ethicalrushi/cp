import heapq

t = int(input())
for _ in range(t):
    s = input()
    r = input()

    n = len(s)
    diff = []
    for i in range(n):
        if s[i]!=r[i]:
            diff.append(i)
    
    if len(diff)==0:
        res=0
    else:
        lheap = []
        for i in range(1,len(diff)):
            lheap.append(diff[i]-diff[i-1])

        heapq.heapify(lheap)

        k= len(diff)
        cl = len(diff)
        res = k*cl
        
        for j in range(k-1,0,-1):
            mn1 = heapq.heappop(lheap)
            cl = cl-1+mn1
            res= min(res,j*cl)

    print(res)




            
