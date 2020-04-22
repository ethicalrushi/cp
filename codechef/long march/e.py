# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#         self.prev = None
    
#     def insert(self, val):



def lcs(X , Y): 
    m = len(X) 
    n = len(Y) 

    L = [[None]*(n+1) for i in range(m+1)] 
    res = [[[]]*(n+1) for i in range(m+1)]
    res1 = [[None]*(n+1) for i in range(m+1)]
    for i in range(m+1): 
        for j in range(n+1): 

            # print(i,j)
            if i == 0 or j == 0 : 
                L[i][j] = 0
                res[i][j] = []
                # print(res1[i])
                res1[i][j] = []
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
                res[i][j] = res[i-1][j-1]+[X[i-1]]
                res1[i][j] = res1[i-1][j-1]+[(i-1,j-1)]
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 
                if L[i-1][j]>L[i][j-1]:
                    res[i][j] = res[i-1][j]
                    res1[i][j] = res1[i-1][j]
                else:
                    res[i][j] = res[i][j-1]
                    res1[i][j] = res1[i][j-1]

    return L[m][n], res[m][n], res1[m][n]
    

        


t = int(input())
for _ in range(t):
    n,k = [int(x) for x in input().strip().split()]
    a = [int(x) for x in input().strip().split()]
    for i in range(1,k):
        b = [int(x) for x in input().strip().split()]
        c, r, ind = lcs(a,b)
        a = r

    res = [0 for i in range(n)]

    for i in range(len(a)-1):
        res[a[i]-1] = a[i+1]
    
    c=0
    for r in res:
        if r==0:
            c+=1
    print(c)
    print(*res)
    
    # print(1)
    # print(*res)
    
