#include<bits/stdc++.h>
using namespace std;

int dp[101][100002];
long long int mod=1e9+7;
int a[101];
int n;

//Recursive dp solution
int solve(int i, int k)
{   cout<<i<<" "<<k<<"\n";

    if((i==n) && (k==0))
        return 1;

    if(i==n)
        return 0;

    if(k<0)
        return 0;

    if(dp[i][k]!=-1)
        return dp[i][k]%mod;

    dp[i][k] = 0;
    for(int j=0;j<=min(k,a[i]);j++)
        dp[i][k]= (dp[i][k] %mod+solve(i+1,k-j)%mod)%mod;
    
    return dp[i][k]%mod;

}

int main()
{
    int k;
    cin>>n>>k;
    // int a[n];

    for(int i=0;i<n;i++)
        cin>>a[i];

    //Initializing dp
    for(int i=0;i<101;i++)
        for(int j=0;j<100002;j++)
            dp[i][j] = -1;

    int res=0;
    res = solve(0,k)%mod;
    // for(int i=0;i<=a[0];i++)
    //     res+=solve(0,k-i,n,a);

    cout<<res<<endl;
}