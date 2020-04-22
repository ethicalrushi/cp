
#include<bits/stdc++.h>
using namespace std;

int main() {
	
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	
	long long int n, k;
	cin>>n>>k;
	map<long long int, long long int>m;
	long long int a[n];
	for(long long int i=0;i<n;i++)
		cin>>a[i];
	
	for(long long int i=0;i<n;i++){
		if(m.find(a[i])==m.end())
			m[a[i]]=0;
		m[a[i]]++;
	}
	
	//stores how much element can mn and mx provide for ith element
	vector<pair<long long int, long long int>>prov; 
	long long int s=0;
	for(auto it:m){
		prov.push_back(make_pair(s,n-s-it.second));
		s+=it.second;
	}
		
	vector<long long int>mncost;
	long long int c=0;
	long long int curr, prev=0, curr_cost=0;
	for(auto it:m){
		if(c!=0){ //skip first
			curr = it.first;
			curr_cost += (curr-prev-1)*c;
			mncost.push_back(curr_cost);
			curr_cost+=c;
			c+=it.second;
			prev=curr;
		}
		else{
			c+=it.second;
			prev = it.first;
		}
	}
	
	vector<long long int>mxcost;
	map<long long int, long long int>::reverse_iterator rit; 
  
    c=0;
    prev=0;
    curr_cost=0;
    for(rit = m.rbegin(); rit != m.rend(); rit++) { 
		if(c!=0){ //skip first
			curr = rit->first;
			curr_cost += abs((curr-prev+1))*c;
			mxcost.push_back(curr_cost);
			curr_cost+=c;
			c+=rit->second;
			prev=curr;
		}
		else{
			c+=rit->second;
			prev = rit->first;
		}
        
    } 
    	
	long long int mn = *min_element(a, a+n);
	long long int mx = *max_element(a, a+n);
	long long int res = 1e18;
	long long int avail, req=k;
	long long int ind=0;
	curr_cost=0;
	long long int l = m.size();
	long long int curr_prov;
	long long int m1,m2;
	
	for(auto it:m){
		avail=it.second;
		req = k-avail;
		
		if(req<=0){ //minimum moves reached
			res=0;
			break;
		}
		
		if(it.first==mn){ //only us mxmoves
			curr_cost = mxcost[l-2];
			curr_cost+=req;
		}
		else if(it.first==mx){ //only use mn moves
			curr_cost = mncost[l-2];
			curr_cost+=req;
		}
		else{
			m1 = mxcost[l-2-ind]+min(req,prov[ind].second);
			long long int req1= req-prov[ind].second;
			if(req1>0){
				m1+=mncost[ind-1]+req1;
			}
			m2 = mncost[ind-1]+min(req,prov[ind].first);
			req1 = req-prov[ind].first;
			if(req1>0){
				m2+=mxcost[l-2-ind]+req1;
			}
			curr_cost = min(m1,m2);
		}
		res = min(res, curr_cost); //taking miniumum
		ind++;
	}
		
	cout<<res<<"\n";
	return 0;
}
