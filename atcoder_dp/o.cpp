    #include <bits/stdc++.h>
    using namespace std;
     
    typedef long long ll;
     
    const ll mod = 1e9+7;
     
    ll dp[22][1<<22];
    int c[22][22];
     
    ll solve(int i,ll b, int n)
    {
    	if(dp[i][b]!=-1)
    		return dp[i][b];
    	
    	if(i==n-1)
    	{
    		for(int j=0;j<n;j++)
    		{
    			if((((1<<j)&b)==0) && (c[i][j]==1))
    			{
    				dp[i][b] =1;
    				return 1;
    			}
    		}
    		return 0;
    	}
    	
    	dp[i][b]=0;
    	for(int j=0;j<n;j++)
    	{	
    		if((((1<<j)&b)==0) && (c[i][j]==1))
    			dp[i][b]= (dp[i][b]%mod+solve(i+1, b|(1<<j),n)%mod)%mod;
    	}
    	return dp[i][b]%mod;
    }
     
    int main() {
    	int n;
    	cin>>n;
    	for(int i=0;i<n;i++)
    		for(int j=0;j<n;j++)
    			cin>>c[i][j];
    			
    	memset(dp,-1,sizeof(dp));
    	cout<<solve(0,0,n)%mod;
    	return 0;
    }