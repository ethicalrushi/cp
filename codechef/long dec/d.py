def solve(a,b,l,d):
    j=0
    k=0
    ans = 0
    res = 0
    for i in range(l):
        if j<d:
            ae = '0'
            j+=1
        else:
            ae = a[k]
            k+=1
        
        if ae=='1' and b[i]=='1':
            ans+=1
            res= max(res, ans+1)
            ans =0
        elif ae=='0' and b[i]=='0':
            ans=0
        else:
            ans+=1
    
    return res

t = int(input())
for _ in range(t):
    a = input()
    b = input()

    flag = False
    if '1' in b:
        flag=True

    #make a smaller
    if len(a) > len(b):
        l = len(a)
        d = l-len(b)
        res = solve(b,a,l,d)
    else:
        l = len(b)
        d = l-len(a)
        res = solve(a,b,l,d)

    if res==0 and flag:
        res = 1

    print(res)