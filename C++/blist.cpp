#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define vvi vector<vector<int>> 
int main()
{
    freopen("blist.in","r",stdin);
    freopen("blist.out","w",stdout);
    int N,M;
    cin>>N;
    vvi p;
    int a,b,c;
    int pre=0;
    for(int i=0;i<N;i++)
    {
        cin>>a>>b>>c;
        p.push_back({a,-1,c});
        p.push_back({b,1,-c});
        
    }
    int ans=0;
    sort(p.begin(),p.end());
    for(auto v:p)
    {
        if(v[1]==-1)
        {
            pre+=v[2];
        }
        else
            pre+=v[2];
        //cout<<v[0]<<" "<<v[1]<<" "<<v[2]<<" "<<pre<<endl;
        ans=max(ans,pre);
    }
    cout<<ans;



}