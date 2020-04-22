t = int(input())

for _ in range(t):
    n , k = [int(x) for x in input().strip().split()]
    if k==1:
        res='a'*(n-2)+'bb'
    else:
        s=2
        i=3
        prev=2
        diff = 2
        while s<k:
            # print(s,i)
            prev=s
            s=s+diff
            diff+=1
            i+=1

        if s>k:
            s = prev
            i-=1
        
        rem = k-s
        # print(n, k, rem, i, s)
        res = ['a' for i in range(n)]
        res[n-i]='b'
        res[n-rem-1]='b'

    print("".join(r for r in res))
    

    
