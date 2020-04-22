#include <bits/stdc++.h> 
#define ll long long 
const int N = 100001; 
using namespace std; 

ll factorialNumInverse[N + 1]; 

ll naturalNumInverse[N + 1]; 

ll fact[N + 1]; 

void InverseofNumber(ll p) 
{ 
	naturalNumInverse[0] = naturalNumInverse[1] = 1; 
	for (int i = 2; i <= N; i++) 
		naturalNumInverse[i] = naturalNumInverse[p % i] * (p - p / i) % p; 
} 

void InverseofFactorial(ll p) 
{ 
	factorialNumInverse[0] = factorialNumInverse[1] = 1; 

	for (int i = 2; i <= N; i++) 
		factorialNumInverse[i] = (naturalNumInverse[i] * factorialNumInverse[i - 1]) % p; 
} 

void factorial(ll p) 
{ 
	fact[0] = 1; 

	for (int i = 1; i <= N; i++) { 
		fact[i] = (fact[i - 1] * i) % p; 
	} 
} 

ll Binomial(ll N, ll R, ll p) 
{ 

	ll ans = ((fact[N] * factorialNumInverse[R]) 
			% p * factorialNumInverse[N - R]) 
			% p; 
	return ans; 
} 


int main() 
{ 
    int t;
    cin>>t;
    ll p = 1000000007; 
    InverseofNumber(p); 
    InverseofFactorial(p); 
    factorial(p); 
    while (t--)
    {
        int n;
        cin>>n;
        string s1,s2;
        cin>>s1;
        cin>>s2;
        int a=0, b=0;
        for(int i=0;i<n;i++)
        {
            if(s1[i]=='1')
                a+=1;
            if(s2[i]=='1')
                b+=1;
        }
        int mn,mx;
        mn = abs(a-b);
        if(a+b>n)
            mx = a+b-2*(a+b-n);
        else
            mx = a+b;

        int res=0;

        for(int i=mn;i<=mx;i+=2)
        {
            res = ((res%p)+Binomial(n,i,p)%p)%p;
        }
        cout<<res<<endl;

    }


	return 0; 
} 
