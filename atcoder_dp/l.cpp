#include <bits/stdc++.h>

using namespace std;

long long int dp[3001][3001][2];

long long int solve(long int a[], int i,int j,int t)
{
	if(dp[i][j][t]!=-1)
		return dp[i][j][t];
		
    else if(i==j)
    {
        int d;
        if(t==0)
            d = -1;
        else
            d = 1;

        dp[i][j][t] = d*a[i];
    }
    else if(t==1)
        dp[i][j][t] = max(solve(a,i+1,j,0)+a[i], solve(a, i,j-1,0)+a[j]);
    else
        dp[i][j][t] = min(solve(a, i+1,j,1)-a[i],solve(a, i,j-1,1)-a[j]);
    
    return dp[i][j][t];
}

int main()
{
    int n;
    cin>>n;
    long int a[n];
    for(int i=0;i<n;i++)
        cin>>a[i];
	
	for(int i=0;i<3000;i++)
		for(int j=0;j<3000;j++)
			for(int t=0;t<2;t++)
				dp[i][j][t] = -1;
				
    cout<<solve(a,0,n-1,1);

    return 0;
    

}