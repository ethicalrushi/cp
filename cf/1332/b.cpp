#include<bits/stdc++.h>
using namespace std;

void solve(){
	int n;
	cin>>n;
	int primes[] = {2,3,5,7,11,13,17,19,23,29,31};
	int a[n];
	for(int i=0;i<n;i++)
		cin>>a[i];
	
	set<int>s;
	vector<int>res;
	for(int i=0; i<n;i++){
		for(int j=0;j<11;j++){
			if(a[i]%primes[j]==0){
				res.push_back(j+1);
				s.insert(j+1);
				break;
			}
		}
	}
	
	cout<<s.size()<<"\n";
	int c=1;
	for(auto e:s){
		for(int i=0;i<n;i++){
			if(res[i]==e){
				res[i]=c;
			}
		}
		c++;
	}
	
	for(auto r:res)
		cout<<r<<" ";
	cout<<"\n";
}
				
				

int main() {
	
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	
	int t;
	cin>>t;
	while(t--)
		solve();
	
	return 0;
	
}
