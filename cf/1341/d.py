num = {}
ar = ["1110111", "0010010", "1011101", "1011011", "0111010", "1101011", "1101111", "1010010", "1111111", "1111011"]
for i in range(len(ar)):
    num[ar[i]] = i
ar = ar[::-1]

n, k = [int(x) for x in input().strip().split()]

init = []
for i in range(n):
    s = input()
    init.append(s)

dp = [[False for j in range(k+1)]for i in range(len(init)+1)]


def solve(i,k):
    if i==n and k==0:
        dp[i][k]=True
        return True

    if i==n:
        dp[i][k]=False
        return False

    if dp[i][k]:
        return dp[i][k]

    for ele in ar:
        flag=True
        diff=0
        for j in range(7):
            if ele[j]=='0' and init[i][j]=='1':
                flag=False
                break
            if init[i][j]!=ele[j]:
                diff+=1
        if flag and k>=diff:
            dp[i][k] = dp[i][k] or solve(i+1,k-diff)

    return dp[i][k]


def get_ans(i,k):
    if i==n and k==0:
        return
    
    if i==n:
        return 
    
    for ele in ar:
        flag=True
        diff=0
        for j in range(7):
            if ele[j]=='0' and init[i][j]=='1':
                flag=False
                break
            if init[i][j]!=ele[j]:
                diff+=1
        if flag and k>=diff:
            if dp[i+1][k-diff]:
                print(num[ele], end="")
                get_ans(i+1,k-diff)
                break

res = solve(0,k)
if res:
    get_ans(0,k)
    print()
else:
    print(-1)
