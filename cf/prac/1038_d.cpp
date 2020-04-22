#include<bits/stdc++.h>
using namespace std;

int main() {
	
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	
	int n;
	cin>>n;
	long long int a[n];
	bool pflag=false, nflag=false;
	long long int res=0;
	for(int i=0;i<n;i++){
		cin>>a[i];
		res+=abs(a[i]);
		if(a[i]>0)
			pflag=true;
		else
			nflag=true;
	}
	long long int ans;
	if(n==1){
		ans=a[0];
	}
	else if(pflag && nflag){
		ans=res;
	}
	else if(pflag){
		int mn = *min_element(a, a+n);
		ans = res-2*mn;
	}
	else{
		int mx = *max_element(a, a+n);
		ans = res-2*abs(mx);
	}
	cout<<ans<<"\n";
		
	return 0;
}
