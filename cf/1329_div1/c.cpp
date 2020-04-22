#include<bits/stdc++.h>
using namespace std;

void solve() {
	int h,g,n,m, s=0;
	cin>>h>>g;
	
	n = pow(2,h)-1;
	m = pow(2,g)-1;

	
	int a[n];
	for(int i=0;i<n;i++){
		cin>>a[i];
		s+=a[i];
	}
	
	pair<int,int>root = make_pair(a[0],0);
	vector<pair<int, int>>l, r; //left and right
	l.push_back(root);
	
	if(n>1){
	
		int ind=1;  //left-subtree
		l.push_back(make_pair(a[1],1));
		while(2*(l[ind].second+1)<n){
			int i=l[ind].second;
			l.push_back(make_pair(a[2*(i+1)-1],2*(i+1)-1));
			l.push_back(make_pair(a[2*(i+1)], 2*(i+1)));
			ind++;
		}
		
		ind=0; //right-subtree
		r.push_back(make_pair(a[2],2));
		while(2*(r[ind].second+1)<n){
			int i=r[ind].second;
			r.push_back(make_pair(a[2*(i+1)-1],2*(i+1)-1));
			r.push_back(make_pair(a[2*(i+1)], 2*(i+1)));
			ind++;
		}
	}

	int i=0,j=0;
	int ct=n-m; 
	vector<int>res;
	bool iflag=true, jflag=false, tj=false, ti=false;
	
	int ni, nj;
	int k1=l.size(), k2=r.size();


	
	while(ct>0){
		
		if(j>=k2){
			//cout<<"c1 b"<<endl;
			s-=l[i].first;
			i+=1;
			res.push_back(1);
		}
		else if(i>=k1){			
			//cout<<"c1 b"<<endl;
			s-=r[j].first;
			j+=1;
			res.push_back(1);
		}
		else{
		
			if(iflag){
				if(i+1<k1){
					if(l[i+1].first>r[j].first){
						ni = i+2; nj=j;ti=true;tj=false;}
					else{
						ni = i+1; nj=j;ti=false;tj=true;}
				}
				else{
					ni = i+1; nj=j;tj=true;ti=false;}
			}
			else{
				if(j+1<k2){
					if(r[j+1].first>l[i].first){
						nj = j+2; ni=i;tj=true;ti=false;}
					else{
						nj = j+1; ni=i;tj=false;ti=true;}
				}
				else{
					nj=j+1; ni=i;ti=true;tj=false;}
			}
			
			
			//cout<<"i, j, ni, nj"<<i<<" "<<j<<" "<<ni<<" "<<nj<<"\n";
			if(iflag){
				if(iflag && k1-ni>=g-1){
					//cout<<"c1 a"<<endl;
					s-=l[i].first;
					res.push_back(1);
					i=i+1;
					j=nj;
					iflag=ti;
					jflag=tj;
					
				}
				else{
					//cout<<"c1 b"<<endl;
					s-=r[j].first;
					j+=1;
					res.push_back(3);
				}
			}
			else{
				
				if(jflag && k2-nj>=g-1){
					//cout<<"c2 a"<<endl;
					s-=r[j].first;
					res.push_back(1);
					i = ni;
					j = j+1;
					iflag = ti;
					jflag = tj;
				}
				else{
					//cout<<"c2 b"<<endl;
					s-=l[i].first;
					i+=1;
					res.push_back(2);
				}	
			}
		}
		
		ct--;
	}
	
	//print answers
	cout<<s<<"\n";
	
	for(auto ans:res)
		cout<<ans<<" ";
		
	cout<<"\n";
}

	

int main() {
	
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	
	int t;
	cin>>t;
	while(t--)
		solve();
	
	return 0;
	
}
