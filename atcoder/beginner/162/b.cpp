#include<bits/stdc++.h>
using namespace std;

int main() {
	
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	
	int n;
	cin>>n;
	long long int res=0;
	for(int i=1;i<=n;i++)
	{
		if(i%3!=0 && i%5!=0)
			res+=i;
	}
	cout<<res<<"\n";
	return 0;
	
}
