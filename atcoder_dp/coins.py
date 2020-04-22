#Try 1-d dp
#Current time complexity O(n^2) can be easily reduced to O(n)
n = int(input())
p = [float(x) for x in input().strip().split()]
dp = [[None for i in range(n//2+2)] for j in range(n)]
for i in range(n):
    dp[i][0] =1

for j in range(n//2+2):
    dp[n-1][j] = 0
dp[n-1][0] = 1
dp[n-1][1] = p[n-1]

for i in range(n-2,-1,-1):
    for j in range(1,n//2+2):
        dp[i][j] = p[i]*dp[i+1][j-1]+(1-p[i])*dp[i+1][j]

print(dp[0][-1])


"""
C++ - some issue with precision

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin>>n;
    double p[n];
    for(int i=0;i<n;i++)
        scanf("%lf", &p[i]);
        
    int t = (n/2)+1;
    double dp[n][t];
    for(int i=0;i<=t;i++)
        dp[n-1][i] = 0;
    dp[n-1][0] = 1;
    dp[n-1][1] = p[n-1];
    
    for(int i=n-2;i>=0;i--)
    {
        for(int j=1;j<=t;j++)
            dp[i][j] = p[i]*dp[i+1][j-1]+(1.0-p[i])*dp[i+1][j];
    }

        
    cout << fixed << setprecision(10) << dp[0][t] << endl;
	return 0;
}
"""

"""
Recursive top down

# def solve(i,k):
#     # print(i,k)
#     if i<=n-1 and k>0 and dp[i][k]:
#         return dp[i][k]
#     if k<=0:
#         # if i not in dp:
#         #     dp[i] ={}
#         # dp[i][k] = 1
#         return 1

#     elif i>n-1:
#         # if i not in dp:
#         #     dp[i] ={}
#         # dp[i][k] = 0
#         return 0
#     elif k>n-i:
#         # if i not in dp:
#         #     dp[i] ={}
#         dp[i][k] = 0

#     else:
#         # if i not in dp:
#         #     dp[i] ={}
#         dp[i][k] = p[i]*solve(i+1,k-1)+(1-p[i])*solve(i+1,k)
#     return dp[i][k]


# print(solve(0,n//2+1))


"""