#include <bits/stdc++.h>
#include <unistd.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;

#define INF 1000000007
#define mem(dp,a) memset(dp,a,sizeof dp)
#define flash ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define rep(i,a,b) for(ll i=a;i<b;i++)
#define repb(i,a,b) for(ll i=a;i>=b;i--)
#define f(i,n) for (ll i=0;i<n;i++)
#define sieve(j,mp) for(ll j=i*i ; j<=mp ; j+=i)
#define pb(x) push_back(x)
#define mp(x,y) push_back(make_pair(x,y))
#define tr(c,it) for(((c).begin())it=(c).begin();it!=(c).end();it++)
#define test ll t=1; cin>>t; while(t--)
#define F first
#define S second
int main()
{
    freopen("input/input03.txt","r",stdin);
    flash
    clock_t launch=clock();
    test
    {
        ll n,mx; cin>>n;
        ll a[n];
        vector<ll> v;
        f(i,n) cin>>a[i];
        sort(a,a+n);
        v.pb(a[0]);
        rep(i,1,n)
        if(a[i]!=a[i-1])
        v.pb(a[i]);
        n=v.size();
        ll s[n];
        mx=v[0];
        s[0]=v[0];
        rep(i,1,n)
        {
            if(v[i]==v[i-1]+1)
            s[i]=v[i]+s[i-1];
            else s[i]=v[i];
            mx=max(mx,s[i]);
        }
        cout<<mx%INF<<endl;
    }
    clog<<((long double)(clock()-launch)/CLOCKS_PER_SEC)<<"\n";
    return 0;
}