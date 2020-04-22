#include <bits/stdc++.h>
using namespace std;

void solve() {
	int n;
	cin>>n;
	string s;
	cin>>s;
	vector<pair<string, int>>vs;
	for(int k=1;k<=n;k++){
		string curr = s.substr(k-1,n+1-k);
		string rem = s.substr(0,k-1);
		if(n%2==k%2)
			reverse(rem.begin(), rem.end());
			
		string temp = curr+rem;
		vs.push_back(make_pair(temp,k));
	}
	
	sort(vs.begin(), vs.end());
	cout<<vs[0].first<<endl;
	cout<<vs[0].second<<endl;

}

int main() {
	
	
	int t;
	cin>>t;
	while(t--){
		solve();
	}
	
	return 0;
}
