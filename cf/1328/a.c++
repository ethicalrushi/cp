    #include<bits/stdc++.h>
     
    using namespace std;
    typedef long long ll;
     
    void Solve()
    {
        ll a,b,ans = b-a;
        cin>>a>>b;
        
        ans = ceil((double)a/(double)b)*b;
        cout<<ans-a<<"\n";    
    }
     
    int main()
    {
        ll t;
        cin>>t;
        while(t--)
            Solve();
    }