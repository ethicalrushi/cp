t = int(input())

for _ in range(t):
    n, k = [int(x) for x in input().strip().split()]
    s = input()

    mat = [[0 for i in range(26)] for j in range(k)]

    i=0
    while i<n:

        j=0
        while j<k:
            char = ord(s[i+j])-97
            mat[j][char]+=1
            j+=1
            
        i+=k

    def fmax(mat,l,h):
        res = 10**20

        for i in range(26):
            temp = n//k-mat[l][i]+n//k-mat[h][i]
            res = min(res, temp)

        if l==h:
            res=res//2
            
        return res

    res=0  
    l = 0
    h = k-1

    while l<=h:
        if l==h:
            res+=fmax(mat,l,l)
            break
        
        res+=fmax(mat,l,h)
        l+=1
        h-=1
    
    print(res)