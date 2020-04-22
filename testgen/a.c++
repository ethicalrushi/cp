#include <bits/stdc++.h>
#include <unistd.h>
#include<stdio.h>
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

int solve(int a[], int n)
{
    unordered_set<int>m;
    for(int i=0;i<n;i++)
        m.insert(a[i]);
    
    int res=0, l=0, ans=0;
    long int mod = 1e9+7;
    for(int i=0;i<n;i++)
    {
        //it is starting number of a seq
        if(m.find(a[i]-1)==m.end())
        {
            l = a[i];
            ans=0;
            while(m.find(l)!=m.end())
            {
                ans = ((ans%mod)+(l%mod))%mod;
                l++;
                // ans++;
            }
            res = max(res,ans);
        }
        
    }
    return res;
}


int main() {
    freopen("input/input03.txt","r",stdin);
    flash
    clock_t launch=clock();
    int t;
    cin>>t;
    // cout<<"t"<<t<<endl;
    while(t--)
    {
        int n;
        // cout<<"n"<<n<<endl;
        cin>>n;
        int a[n];
        for(int i=0;i<n;i++)
            cin>>a[i];
        //cout<<solve(a,n)<<endl;
        unordered_set<int>m;
        for(int i=0;i<n;i++){
            if(m.find(a[i])==m.end())
                m.insert(a[i]);
        }
            
        
        int res=0, l=0, ans=0;
        long int mod = 1e9+7;
        for(int i=0;i<n;i++)
        {
            //it is starting number of a seq
            if(m.find(a[i]-1)==m.end())
            {
                l = a[i];
                ans=0;
                while(m.find(l)!=m.end())
                {
                    ans = ((ans)+(l));
                    l++;
                    // ans++;
                }
                res = max(res,ans);
            }
            
        }
        cout<<res%mod<<endl;
    }
    clog<<((long double)(clock()-launch)/CLOCKS_PER_SEC)<<"\n";
    return 0;
}