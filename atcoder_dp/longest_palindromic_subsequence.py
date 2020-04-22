s = input()
n = len(s)

L = [[None for i in range(n+1)] for j in range(n+1)]
def lcs(i,j):
    if L[i][j]:
        return L[i][j]
    if i==j:
        L[i][j] =1
        return L[i][j]
    if s[i]==s[j]:
        if i+1==j:
            L[i][j] = 2
        else:
            L[i][j] = 2+lcs(i+1,j-1)
    else:
        L[i][j] = max(lcs(i+1,j),lcs(i,j-1))

    return L[i][j]

return(lcs(0,n-1))

print(lcs(0,n-1))