#include<bits/stdc++.h>
using namespace std;

long long int power(long long int x, long long int y, long long int p)  {
	long long int res = 1;  
    x = x % p; 
    if (x == 0) return 0; 
  
    while (y > 0)  
    {  
        if (y & 1)  
            res = (res*x) % p;  
        y = y>>1; 
        x = (x*x) % p;  
    }  
    return res;  
}   

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
