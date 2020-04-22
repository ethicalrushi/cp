#include <bits/stdc++.h>
using namespace std;

int main() {
	int n, t;
	cin>>n;
	vector<int>a;
	vector<int>b;
	vector<int>c;
	
	for(int i=0;i<n;i++){
		cin>>t;
		a.push_back(t);
	}
		
		
	for(int i=0;i<n;i++){
		cin>>t;
		b.push_back(t);
	}
	
	for(int i=0;i<n;i++){
		c.push_back(a[i]-b[i]);
	}
	
	sort(c.begin(), c.end());
	int ind, res=0;
	for(int i=0;i<n;i++){
		int e = c[i];
		
		if(e<0){
			ind = lower_bound(c.begin(), c.end(), -1*e+1)-c.begin();
		}
		else if(e==0)
			ind = lower_bound(c.begin(), c.end(), 1)-c.begin();
		else
			ind = i+1;
			
		res+= (n-ind);
	}
	
	cout<<res<<endl;
	
	return 0;
}