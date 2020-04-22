#include<bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    long long int n,k,res;

    cin>>n>>k;
    res = n;
    for(long int i=0;i<50000000;i++){
        n = abs(n-k);
        res = min(res, n);
    }
    cout<<res<<endl;
}