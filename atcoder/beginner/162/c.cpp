#include<bits/stdc++.h>
using namespace std;

int main() {
	
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	
	int k;
	cin>>k;
	long long int res=0;
	
	for(int i=1;i<=k;i++){
		for(int j=1;j<=k;j++){
			for(int c=1;c<=k;c++)
			{
				res+= __gcd(i,__gcd(j,c));
				//cout<<i<<" "<<j<<" "<<c<<" "<<__gcd(i,__gcd(j,k))<<endl;
				//cout<<res<<" ";
			}
		}
	}
	cout<<res<<"\n";
	
	return 0;
	
}
