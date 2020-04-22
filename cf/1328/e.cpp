#include<bits/stdc++.h>
using namespace std;

vector<vector<int>>tree;
int T;
int depth[200005];
int parent[200005];
vector<int> tin, tout;

void height(int src, int par, int d){
	depth[src] = d;
	parent[src] = par;
	tin[src]=T++;
	for(auto child:tree[src])
		if(child!=par)
			height(child, src, d+1);
	
	tout[src]=T++;
}

/** any node in subtree of v will have 
 * tin[v]>=tin[u] && tou[v]<=tout[u]
 **/
 
bool isAnc(int v, int u) { //returns true if v is insubtree of u
	return tin[v] <= tin[u] && tout[u] <= tout[v];
}

/** Too much memory consuming, instad use time in and time out approach
void bfs(int node) 
{ 
    queue<pair<int, int> > qu; 
    qu.push({ node, -1 });
  
    while (!qu.empty()) { 
        pair<int, int> p = qu.front(); 
        qu.pop(); 
        path[p.first].push_back(p.first);
  
        for (auto child : tree[p.first]) { 
            if (child!=p.second) { 
                qu.push({ child, p.first }); 
                path[child] = path[p.first]; 
            } 
        } 
    } 
} 
  
 **/

int main() {
	
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
 
	int n,m,q,u,v;
	cin>>n>>q;
	tree = vector<vector<int>>(n+1);
	T = 0; //initalize time as 0
	tin = tout = vector<int>(n+1);
	for(int i=1;i<n;i++){
		cin>>u>>v;
		tree[u].push_back(v);
		tree[v].push_back(u);
	}
	
	height(1,-1,0);
	
	while(q--){
		cin>>m;
		int a[m];
		int mx=-1;
		int node;
		for(int i=0;i<m;i++){
			cin>>a[i];
			if(depth[a[i]]>mx){
				mx=depth[a[i]];
				node=a[i];
			}
		}
		
		bool flag=true;
		
		//convert all nodes except deepest node to thier parents, 
		//now all converted nodes and deepest node have to lie on same path
		for(int i=0;i<m;i++){
			if(parent[a[i]]!=-1 && a[i]!=node)
				a[i] = parent[a[i]];
		}
		
		/** It is sufficient to prove that deepest node lies 
		 * in subtree of every other node, so that all make one single path
		 **/
		
		for(int i=0;i<m;i++)
			flag &=isAnc(a[i],node);
		
		if(flag)
			cout<<"YES\n";
		else
			cout<<"NO\n";
	}
	
	return 0;
	
}
