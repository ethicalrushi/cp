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
	
	int n;
	cin>>n;
	long long int mod = 998244353;
	vector<long long int>res;
	
	res.push_back(10); //i=n
	long long int s=1, ncurr =0, curr=0;
	for(int i=n-1;i>=1;i--){
		if (s+1-2>0){
			curr = (81*power(10,n-i-2,mod))%mod;
			curr = ((curr%mod) * ((s+1-2)*10)%mod)%mod;
		}
		ncurr = (9*power(10,n-i-1,mod))%mod;
		ncurr = ((ncurr%mod) * ((2)*10)%mod)%mod;
		curr = (curr%mod + ncurr%mod)%mod;
		res.push_back(curr);
		s++;
	}
	reverse(res.begin(), res.end());
	for(auto r:res)
		cout<<r<<" ";
	cout<<"\n";
	return 0;
	
}
