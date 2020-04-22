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
vector <int> g[MAXN];   
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
    cout<<"reached fun"<<n<<" "<<prime.size()<<endl;
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
    
    cout<<"completed"<<endl;
    return res;
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

void compute_cost(int curr, int prev, unordered_map<int, int>prevfactor) {

    cout<<"trying to compute"<<endl;

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



// int n;
// vector<vector<int>> adj;



// void dfs(int curr, int curr_depth, int n) {
//     stack<pair<int, int>>st;
//     st.push(make_pair(curr, curr_depth));
//     vector<int>ptr(n+1,0);
//     vector<int>parent(n+1,-1);

//     while(!st.empty()) {
//         curr = st.top().first;
//         curr_depth = st.top().second;
//         euler_tour.push_back(curr);
//         height[curr] = curr_depth;

//         st.pop();

//         int k = tree[curr].size();
//         while(ptr[curr]<k && tree[curr][ptr[curr]]==parent[curr])
//             ptr[curr]+=1;

//         if(ptr[curr]==k){
//             if(parent[curr]!=-1)
//                 st.push(make_pair(parent[curr], curr_depth-1));
//         }
//         else
//         {
//             int node = tree[curr][ptr[curr]];
//             st.push(make_pair(node,curr_depth+1));
//             ptr[curr]+=1;
//             parent[node] = curr;
//         }

//     }

// }

int block_size, block_cnt;
vector<int> first_visit;
vector<int> euler_tour;
vector<int> height;
vector<int> log_2;
vector<vector<int>> st;
vector<vector<vector<int>>> blocks;
vector<int> block_mask;

void dfs1(int v, int p, int h) {
    first_visit[v] = euler_tour.size();
    euler_tour.push_back(v);
    height[v] = h;

    for (int u : tree[v]) {
        if (u == p)
            continue;
        dfs1(u, v, h + 1);
        euler_tour.push_back(v);
    }
}

int min_by_h(int i, int j) {
    return height[euler_tour[i]] < height[euler_tour[j]] ? i : j;
}

void precompute_lca(int root, int n) {
    // get euler tour & indices of first occurences
    first_visit.assign(n, -1);
    height.assign(n, 0);
    euler_tour.reserve(2 * n);
    dfs(root, 0, n);
    cout<<"dfs calculated"<<endl;
    for(int i=0;i<euler_tour.size();i++)
        cout<<euler_tour[i]<<" ";
    
    cout<<endl;
    for(int i=0;i<=n;i++)
        cout<<height[i]<<" ";
    cout<<endl;
    // precompute all log values
    int m = euler_tour.size();
    log_2.reserve(m + 1);
    log_2.push_back(-1);
    for (int i = 1; i <= m; i++)
        log_2.push_back(log_2[i / 2] + 1);

    block_size = max(1, log_2[m] / 2);
    block_cnt = (m + block_size - 1) / block_size;

    // precompute minimum of each block and build sparse table
    st.assign(block_cnt, vector<int>(log_2[block_cnt] + 1));
    for (int i = 0, j = 0, b = 0; i < m; i++, j++) {
        if (j == block_size)
            j = 0, b++;
        if (j == 0 || min_by_h(i, st[b][0]) == i)
            st[b][0] = i;
    }
    for (int l = 1; l <= log_2[block_cnt]; l++) {
        for (int i = 0; i < block_cnt; i++) {
            int ni = i + (1 << (l - 1));
            if (ni >= block_cnt)
                st[i][l] = st[i][l-1];
            else
                st[i][l] = min_by_h(st[i][l-1], st[ni][l-1]);
        }
    }

    // precompute mask for each block
    block_mask.assign(block_cnt, 0);
    for (int i = 0, j = 0, b = 0; i < m; i++, j++) {
        if (j == block_size)
            j = 0, b++;
        if (j > 0 && (i >= m || min_by_h(i - 1, i) == i - 1))
            block_mask[b] += 1 << (j - 1);
    }

    // precompute RMQ for each unique block
    int possibilities = 1 << (block_size - 1);
    blocks.resize(possibilities);
    for (int b = 0; b < block_cnt; b++) {
        int mask = block_mask[b];
        if (!blocks[mask].empty())
            continue;
        blocks[mask].assign(block_size, vector<int>(block_size));
        for (int l = 0; l < block_size; l++) {
            blocks[mask][l][l] = l;
            for (int r = l + 1; r < block_size; r++) {
                blocks[mask][l][r] = blocks[mask][l][r - 1];
                if (b * block_size + r < m)
                    blocks[mask][l][r] = min_by_h(b * block_size + blocks[mask][l][r], 
                            b * block_size + r) - b * block_size;
            }
        }
    }
}

int lca_in_block(int b, int l, int r) {
    return blocks[block_mask[b]][l][r] + b * block_size;
}

int lca(int v, int u) {
    int l = first_visit[v];
    int r = first_visit[u];
    if (l > r)
        swap(l, r);
    int bl = l / block_size;
    int br = r / block_size;
    if (bl == br)
        return euler_tour[lca_in_block(bl, l % block_size, r % block_size)];
    int ans1 = lca_in_block(bl, l % block_size, block_size - 1);
    int ans2 = lca_in_block(br, 0, r % block_size);
    int ans = min_by_h(ans1, ans2);
    if (bl + 1 < br) {
        int l = log_2[br - bl - 1];
        int ans3 = st[bl+1][l];
        int ans4 = st[br - (1 << l)][l];
        ans = min_by_h(ans, min_by_h(ans3, ans4));
    }
    return euler_tour[ans];
}























int main() {
    //assert(freopen("input.txt","r",stdin));
    //assert(freopen("output.txt","w",stdout));  

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    prime = SieveOfEratosthenes(1e3+5);
    m = prime.size();

    ll mod=1e9+7;

    int t, n, u, v, root, q, pivot;
    ll res;
    int a[n];
    cin>>t;
    unordered_map<int, int>initfactor;
    while(t--){
        cin>>n;

        //flush tree
        for(int i=0;i<MAXN;i++){
            vector<int>temp;
            tree[i] = temp;
        }

        // //flush costs, factors
        // for(int i=0;i<MAXN;i++){
        //     cost[i] = initfactor;
        // }

        // factors.clear();
        // factors.push_back(initfactor);

        for(int i=0;i<n-1;i++){
            cin>>u>>v;
            tree[u].push_back(v);
            tree[v].push_back(u);
        }

        // //cost input
        // for(int i=0;i<n;i++)
        //     cin>>a[i];
            
        // cout<<"assigning factors"<<endl;
        // // factors[1] = assign_factors(a[0]);
        // // cout<<factors[1].size()<<"1 dine"<<endl;
        // for(int i=0;i<n;i++){
        //     factors.push_back(assign_factors(a[i]));
        //     // cout<<factors[i+1].size()<<endl;
        // }
        
        // cout<<"before computing call"<<endl;
        // compute_cost(1,0,initfactor);

        // cout<<"cost computed"<<endl;
        precompute_lca(1,n);

        cin>>q;

        while(q--){

            cin>>u>>v;
            pivot = lca(u,v);
            cout<<"pivot "<<pivot<<endl;
        }
    }

    return 0;
}