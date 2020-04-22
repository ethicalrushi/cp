#include<bits/stdc++.h>

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t, n, k;
    int coupled[100005];
    int g1;
    bool gflag;
    cin>>t;
    int t1;
    while(t--) {
        cin>>n;
        gflag=false;
        bool cflag=false;

        for(int i=0;i<=n;i++)
            coupled[i]=0;
        
        for(int i=0;i<n;i++){
            cin>>k;
            cflag=false;
            for(int j=0;j<k;j++){
                cin>>t1;
                if(!cflag && coupled[t1]==0){
                    coupled[t1]=1;
                    cflag=true;
                }
            }
            if(!cflag){
                gflag=true;
                g1 = i+1; //unmarried girl
            }
        }

        if(gflag){
            cout<<"IMPROVE\n";
            int b1;
            for(int i=1;i<=n;i++){
                if(coupled[i]==0){
                    b1=i;
                    break;
                }
            }
            cout<<g1<<" "<<b1<<"\n";
        }
        else
        {
            cout<<"OPTIMAL\n";
        }
        
    }


    return 0;
}