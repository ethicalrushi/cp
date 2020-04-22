#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <cassert>
#include <utility>
#include <iomanip>
#include<unordered_map>


using namespace std;

typedef long long int ll;


const int MAXN = 100005;  //try decreasing
const int MAXLOG = 20;

int n, qn;
 
int dp[MAXN][MAXLOG];
int tin[MAXN], tout[MAXN];
int timer;


int m;
vector<int> tree[MAXN];
vector<int>prime;
vector<unordered_map<int, int>>factors;
unordered_map<int, int> cost[MAXN];

vector<int> SieveOfEratosthenes(int n) 
{ 
    bool prime[n+1]; 
    memset(prime, true, sizeof(prime)); 
  
    for (int p=2; p*p<=n; p++) 
    { 
        if (prime[p] == true) 
        { 
            for (int i=p*p; i<=n; i += p) 
                prime[i] = false; 
        } 
    } 
    vector<int>res;
    for (int p=2; p<=n; p++) 
       if (prime[p]) 
          res.push_back(p);

    return res;
} 

//function to calculate power of primes for a number
unordered_map<int, int> assign_factors(int n){
    unordered_map<int, int>res;
    for(int i=0;i<m;i++){
        int count=0;
        while(n%prime[i]==0){
            n=n/prime[i];
            count+=1;
        }
        res[prime[i]]=count;
    }
    if(n>1)
        res[n]=1; //to deal with primes
    
    return res;
}


void dfs(int v, int par=1) {
    stack<int>st;
    st.push(v);
    while(!st.empty()){
        v = st.top();
        st.pop();
        timer++;
        tin[v] = timer;


    }

}

bool isParent(int a, int b) {
    return tin[a] <= tin[b] && tout[a] >= tout[b];
}

int lca(int a, int b) {
    if (isParent(a, b))
        return a;
    if (isParent(b, a))
        return b;
    for (int i = MAXLOG - 1; i >= 0; i--) { 
        if (!isParent(dp[a][i], b))
            a = dp[a][i];
    }
    return dp[a][0];
}

unordered_map<int,int> map_addition(unordered_map<int, int>m1, unordered_map<int, int>m2) {
    unordered_map<int, int> res;

    for(auto it:m1) {
        if(m2.find(it.first)==m2.end())
            res[it.first] = it.second;
        else
            res[it.first] = it.second+m2[it.first];
    }

    for(auto it:m2) {
        if(res.find(it.first)==res.end())
            res[it.first] = it.second;
    }

    return res;
}

unordered_map<int,int> map_subtraction(unordered_map<int, int>m1, unordered_map<int, int>m2) {
    unordered_map<int, int> res;

    for(auto it:m1) {
        if(m2.find(it.first)==m2.end())
            res[it.first] = it.second;
        else
            res[it.first] = it.second-m2[it.first];
    }
    return res;
}


void compute_cost(int curr, int prev, unordered_map<int, int>prevfactor) {

    // cout<<"trying to compute"<<endl;

    stack<tuple<int,int,unordered_map<int, int>>>st;
    st.push(make_tuple(curr, prev, prevfactor));
    int ncurr, nprev;
    unordered_map<int,int>nprevfactor;
    while(!st.empty()){
        tie(ncurr, nprev, nprevfactor) = st.top();
        st.pop();
        cost[ncurr] = map_addition(factors[ncurr],nprevfactor);

        for(int i=0;i<tree[ncurr].size();i++){
            if(tree[ncurr][i]!=nprev)
                st.push(make_tuple(tree[ncurr][i],ncurr,cost[ncurr]));
        }
    }
}


int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    prime = SieveOfEratosthenes(1e3+5);
    m = prime.size();

    ll mod=1e9+7;

    int t, n, u, v, root, q, pivot;
    ll res;
    cin>>t;
    unordered_map<int, int>initfactor;
    while(t--){
        cin>>n;

        if(n==1){
            int a;
            cin>>a;
            unordered_map<int, int>dicres = assign_factors(a);
            res = 1;

            for(auto d:dicres)
                res = ((res%mod)*(d.second+1)%mod)%mod;
            cin>>q;
            while(q--){
                cin>>u>>v;
                cout<<res%mod<<"\n";
            }
        }
        else{
            int a[n];

            //flush tree
            for(int i=0;i<MAXN;i++){
                vector<int>temp;
                tree[i] = temp;
            }

            //flush costs
            for(int i=0;i<MAXN;i++){
                cost[i] = unordered_map<int, int>();
            }

            //flush factors
            factors.clear();
            factors.push_back(unordered_map<int,int>()); //1 indexed

            for(int i=0;i<n-1;i++){
                cin>>u>>v;
                tree[u].push_back(v);
                tree[v].push_back(u);
            }

            //cost input
            for(int i=0;i<n;i++)
                cin>>a[i];
                
            for(int i=0;i<n;i++)
                factors.push_back(assign_factors(a[i]));

            compute_cost(1,0,initfactor);

            dfs(1);


            cin>>q;

            while(q--){
                cin>>u>>v;
                pivot = lca(u,v);
                // cout<<"pivot "<<u<<" "<<v<<" "<<pivot<<endl;
                
                unordered_map<int, int>dic1 = map_subtraction(cost[v],cost[pivot]);
                unordered_map<int, int>dic2 = map_subtraction(cost[u], cost[pivot]);
                unordered_map<int, int>dicres = map_addition(dic1, dic2);
                dicres = map_addition(dicres, factors[pivot]);

                res=1;

                for(auto d:dicres)
                    res = ((res%mod)*(d.second+1)%mod)%mod;
                
                cout<<res%mod<<"\n";
            }
        }
    }

    return 0;
}