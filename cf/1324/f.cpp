#include<bits/stdc++.h>
using namespace std;
int dp[200005];
int a[200005];
int res[200005];
vector<int>tree[200006];

int dfs(int i, int par){
	int add;
	if(a[i-1]==1)
		add=1;
	else
		add=-1;
		
	dp[i] = add;
	for(auto node:tree[i]){
		if(node!=par)
			dp[i] += max(dfs(node,i), 0); //add only if positive
	}

	return dp[i];
}

void solve(int i, int par){ //rerooting concept
	res[i] = dp[i];
	for(auto v:tree[i]){ //trying all possible roots
		if(v!=par){ //rooting at v
			dp[i]-=max(0,dp[v]); //since v is no more child of i
			dp[v]+=max(0,dp[i]); //since i is child of v now
			solve(v,i);
			dp[v]-=max(0,dp[i]); //restoring to try other cjilds of i as root
			dp[i]+=max(0,dp[v]);
		}
	}		
}
	
	

int main() {
	
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	
	int n,u,v;
	cin>>n;
	for(int i=0;i<n;i++)
		cin>>a[i];
	
	for(int i=0;i<n-1;i++){
		cin>>u>>v;
		tree[v].push_back(u);
		tree[u].push_back(v);
	}
	dfs(1,-1);
	solve(1,-1);
	for(int i=1;i<=n;i++)
		cout<<res[i]<<" ";
	cout<<"\n";
	
	return 0;
	
}
