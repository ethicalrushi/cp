#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    long long int u, v, res=0;
    cin>>n;
    vector<pair<long long int, long long int>>a;
    for(int i=0;i<n;i++){
        cin>>u>>v;
        a.push_back(make_pair(u,v));
    }

    if(n==1)
        res = a[0].first;
    else{
        int si=-1;
        long long int mn;
        long long int diff= a[0].first-max(0ll,(a[0].first-a[n-1].second));
        mn = diff;
        si=0;

        for(int i=1;i<n;i++){
            diff = a[i].first-max(0ll,a[i].first-a[i-1].second);
            if(diff<mn){
                mn = diff;
                si=i;
            }
        }

        int ct=1;
        res+=a[si].first;
        int prev_i = si;
        int i=si+1;
        if(i==n)
            i=0;

        while(ct<n){
            res+= max(0ll,a[i].first-a[prev_i].second);
            prev_i = i;
            i++;
            if(i==n)
                i=0;
            ct++;
        }
    }
    cout<<res<<"\n";
}

int main() {
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	
	int t;
	cin>>t;
	while(t--){
		solve();
	}
	
	return 0;
}
