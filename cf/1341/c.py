def solve(a,d):
    n = len(a)
    i = n-1
    while i>=0 and a[i]==d:
        i-=1
        d+=1
    
    if i>0:
        num = d
        c = a[0:i+1]

        gind = c.index(num)
        flag=True
        for j in range(gind+1,len(c)):
            if c[j]!=c[j-1]+1:
                flag = False
                break

        if flag:
            return solve(c[:gind],c[-1]+1)
        else:
            return False
        
    else:
        return True
        

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    flag = solve(a,1)
    
    
    if flag:
        print("Yes")
    else:
        print("No")