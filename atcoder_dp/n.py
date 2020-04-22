n = int(input())
a = [int(x) for x in input().strip().split()]

#stores min cost for creating i-j
c = [[None for i in range(n)] for j in range(n)]

#stores size of i-j combined
s = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    c[i][i] = 0
    s[i][i] = a[i]

for i in range(n):
    for j in range(i+1,n):
        s[i][j] = s[i][j-1]+a[j]

def solve(i,j):
    if c[i][j] is not None:
        return c[i][j]
    mn = 10**100
    for k in range(i,j):
        mn = min(mn,solve(i,k)+solve(k+1,j)+s[i][k]+s[k+1][j])
    c[i][j] = mn
    return c[i][j]

print(solve(0,n-1))
