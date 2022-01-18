#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define vii vector<pair<int,int>> 
int main()
{
    freopen("triangles.in","r",stdin);
    freopen("triangles.out","w",stdout);
    int N,M;
    cin>>N;
    unordered_map<int,vector<int>> XX;
    unordered_map<int,vector<int>> YY;
    vector<pair<int,int>> pos;
    for(int i=0;i<N;i++)
    {
        int x,y;
        cin>>x>>y;
        XX[x].push_back(y);
        YY[y].push_back(x);
        pos.push_back(make_pair(x,y));
    }
    int ans;
    for (pair<int,int> p:pos)
    {
        int x=p.first;
        int y=p.second;
        for(int p:XX[x])
        for(int q:YY[y])
        
            ans=max(ans,abs(p-y)*abs(q-x));
        
    }
    cout<<ans;

       //cout<<endl<<vcc.size();
}