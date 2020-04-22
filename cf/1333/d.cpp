#include<bits/stdc++.h>
using namespace std;

int main() {
	
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	
	int n,k;
	cin>>n>>k;
	string s;
	cin>>s;
	vector<vector<int>>ind;
	int mn=0, mx=0;
	
	while(true){
		mn++;
		ind.push_back(vector<int>());
		for(int i=0;i<n-1;i++){
			if(s[i]=='R' && s[i+1]=='L'){
				ind.back().push_back(i+1);
				mx++;
			}
		}
		
		if(ind.back().size()==0){
			mn--;
			ind.pop_back();
			break;
		}
		for(int x:ind.back())
			swap(s[x],s[x-1]);
	}
	if(k>=mn && k<=mx){
		int extra = k-mn;
		int j=0;
		int ele;
		while(extra--){
			if(ind[j].size()>1){
				ele = ind[j].back();
				ind[j].pop_back();
				cout<<"1 "<<ele<<"\n";
			}
			else if(ind[j].size()==1){ //for size 1 we are not providing any extra step
				ele = ind[j].back();   //it would take 1 step either serially or parallely
				ind[j].pop_back();     //hence add 1 to extra, i.e don't consider it in extra
				cout<<"1 "<<ele<<"\n";
				extra++;
			}
			else{
				j++;
				extra++;
			}
		}
		
		if(ind[j].size()==0)
			j++;
			
		for(int m=j;m<int(ind.size());m++){
			cout<<ind[m].size()<<" ";
			for(int a:ind[m])
				cout<<a<<" ";
			cout<<"\n";
		}
			
	}
	else
		cout<<"-1\n";
	
	return 0;
	
}
