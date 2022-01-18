#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define vii vector<pair<int,int>> 
int main()
{
    //freopen("measurement.in","r",stdin);
    //freopen("measurement.out","w",stdout);
    int N;
    cin>>N;
    int day;
    char name;
    int x,y;
    int idd;
    string change;
    vector<vector<int>> east;
    vector<vector<int>> north;
    
    for(auto i=0;i<N;i++)
    {
        cin>>name>>x>>y;

        if(name=='E')
        {
            east.push_back({x,y,i});
        }

        else 
            north.push_back({x,y,i});
        
    }
    vector<vector<int>> cross;
    for(vector<int> ve:east)
        for(vector<int> vn:north)
        {
            int xx,yy;
            xx=vn[0];
            yy=ve[1];
            
            if(xx>=ve[0] and yy>=vn[1])
            {
                cross.push_back({xx-ve[0],xx,yy,ve[2]});
                cross.push_back({yy-vn[1],xx,yy,vn[2]});
            }
        }
    sort(cross.begin(),cross.end());
    map<pair<int,int>,int> um;
    long long ans[N];
    for(auto i=0;i<N;i++)
        ans[i]=-1;
    for(vector<int> vv:cross){
        int xx,yy;
        xx=vv[1];
        yy=vv[2];
        int ii=vv[3];
        int nn=vv[0];
        if(ans[ii]>0)
            continue;
        if(um.count(make_pair(xx,yy))>0 and um[make_pair(xx,yy)]<nn){
            ans[ii]=nn;
        }
        else{
            um[make_pair(xx,yy)]=nn;
        }
    }
    for(int k:ans)
    {
        if(k<0)
            
   cout<<"Infinity"<<endl;
    else            
   cout<<k<<endl;
    }
}