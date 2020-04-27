#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
# define mod 1000000007
# define MAX_N 1000010
 
const ll INF = ll(1e18)+1;
vector<ll> a(200020);
ll n, k;
 
bool is_ok(ll x){
    ll num_pair = 0;
    for(ll i=0; i<n; i++){
        ll fix = a[i];
        ll l = -1, r = n;
        if(fix >= 0){
            while(r - l > 1){
                ll mid = (l + r) / 2;
                if(fix * a[mid] < x){
                    l = mid;
                }
                else{
                    r = mid;
                }
            }
            num_pair += r;
        }
        else{
            while(r - l > 1){
                ll mid = (l + r) / 2;
                if(fix * a[mid] < x){
                    r = mid;
                }
                else{
                    l = mid;
                }
            }
            num_pair += (n-r);
        }
        if(a[i] * a[i] < x) num_pair--;
    }
    num_pair /= 2;
    return num_pair < k;
}
 
int main(){
int t;
cin>>t;
while(t--)
{
 
    cin >> n >> k;
    a.resize(n);
    for(int i=0; i<n; i++){
        cin >> a[i];
    }
    sort(a.begin(), a.end());
 
    ll l = -INF, r = INF;
    while(r - l > 1){
        ll middle = (l + r) / 2;
        if(is_ok(middle)){
            l = middle;
        }
        else{
            r = middle;
        }
    }
    cout << l << "\n";
}    return 0;
}