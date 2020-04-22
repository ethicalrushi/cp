#include<bits/stdc++.h>

using namespace std;

size_t popcount(size_t n) {
    std::bitset<sizeof(size_t) * CHAR_BIT> b(n);
    return b.count();
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    while (t--)
    {
        int n, q;
        cin>>n>>q;
        long long int a[n];
        for(int i=0;i<n;i++)
            cin>>a[i];

        int e=0, o=0;

        for(int i=0;i<n;i++) {
            int ele = popcount(a[i]);
            if(ele%2==0)
                e+=1;
            else
                o+=1;
        }
        bool flag=false;

        while (q--)
        {
            int p;
            cin>>p;
            int pe = popcount(p);
            if(pe%2==0)
                flag=true;
            else
                flag = false;

            if(flag)
                cout<<e<<" "<<o<<"\n";
            else
                cout<<o<<" "<<e<<"\n";
            
        }
        

    }
    
}