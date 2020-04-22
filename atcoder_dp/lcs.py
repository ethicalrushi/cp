s = input()
t = input()

def lcs(X , Y): 
    m = len(X) 
    n = len(Y) 
  
    L = [[None]*(n+1) for i in range(m+1)] 
    res = [['']*(n+1) for i in range(m+1)]
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
                res[i][j] = ''
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
                res[i][j] = res[i-1][j-1]+X[i-1]
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 
                if L[i-1][j]>L[i][j-1]:
                    res[i][j] = res[i-1][j]
                else:
                    res[i][j] = res[i][j-1]
  
    return L[m][n], res[m][n]

c, r = lcs(s,t)
print(r)


""""
Universal lcs for count, string and indices of matching letters:
Check shortes_common_subsequence problem(leetcode)  for usage example


def lcs(X , Y): 
    m = len(X) 
    n = len(Y) 
  
    L = [[None]*(n+1) for i in range(m+1)] 
    res = [['']*(n+1) for i in range(m+1)]
    res1 = [[None]*(n+1) for i in range(m+1)]
    for i in range(m+1): 
        for j in range(n+1): 
            # print(i,j)
            if i == 0 or j == 0 : 
                L[i][j] = 0
                res[i][j] = ''
                # print(res1[i])
                res1[i][j] = []
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
                res[i][j] = res[i-1][j-1]+X[i-1]
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

"""