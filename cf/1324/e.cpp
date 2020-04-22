#include <bits/stdc++.h>
using namespace std;

long long int n,h,l,r;
long long int a[2100];
long long int dp[2100][2100];
long long int add(int a, int b) {
	if(a+b<=h)
		return a+b;
	return (a+b)%h;
}


long long int solve(int i, int t){
    cout<<i<<" "<<t<<endl;
    // cout<<i<<" "<<t<<endl;
	if(i==n){
        if(t>=l && t<=r)
            return 1;
        return 0;
    }
		
	if(dp[i][t]!=-1)
		return dp[i][t];
		
	long long int t1 = add(t, a[i]-1);
	long long int t2 = add(t, a[i]);
	long long int h1, h2;

    if(t>=l && t<=r){
        h1 = 1+solve(i+1,t1);
        h2 = 1+solve(i+1,t2);
    }
    else
    {
        h1 = solve(i+1, t1);
        h2 = solve(i+1, t2);
    }
    

    // if(t1>=l and t1<=r){
    //     h1 = 1+solve(i+1,t1);
    // }
    // else{
    //     h1 = solve(i+1, t1);
    // }

    // if(t2>=l and t2<=r){
    //     h2 = 1+solve(i+1,t2);
    // }
    // else{
    //     h2 = solve(i+1, t2);
    // }
    
    dp[i][t] =  max(h1, h2);
    return dp[i][t];
	
}

int main() {
	// your code goes here
	cin>>n>>h>>l>>r;
	for(int i=0;i<n;i++)
		cin>>a[i];
		
	for(int i=0;i<2100;i++)
		for(int j=0;j<2100;j++)
			dp[i][j]=-1;
			
	cout<<solve(0,0)<<endl;
	return 0;
}