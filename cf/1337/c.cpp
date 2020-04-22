#include <bits/stdc++.h>
using namespace std;
int mx = 2e5+10;
int depth[200005];
int dp[200005];

vector<int>tree[200005];

int dfs(int node, int d, int par){
    dp[node]=1;
    depth[node]=d;
    for(int i=0;i<tree[node].size();i++){
        if(tree[node][i]!=par)
            dp[node]+=dfs(tree[node][i],d+1,node);

    }
    return dp[node];
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k,u,v;
    cin>>n>>k;
    
    for(int i=0;i<n-1;i++){
        cin>>u>>v;
        tree[u].push_back(v);
        tree[v].push_back(u);
    }

    dfs(1,0,-1);

    vector<int>a;
    for(int i=1;i<=n;i++)
        a.push_back(depth[i]-dp[i]+1);

    sort(a.begin(), a.end(), greater<int>());

    long long int res=0;
    for(int i=0;i<k;i++)
        res+=a[i];

    cout<<res<<"\n";

    return 0;
}