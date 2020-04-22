#include<bits/stdc++.h>
using namespace std;

int main() {
	
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	
	string s;
	cin>>s;
	bool flag=false;
	for(int i=0;i<3;i++){
		if(s[i]=='7')
			flag=true;
			
	}
			
	if(flag)
		cout<<"Yes\n";
	else
		cout<<"No\n";
	
	return 0;
	
}
