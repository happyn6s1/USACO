#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define vii vector<pair<int,int>> 
int main()
{
    freopen("mowing.in","r",stdin);
    freopen("mowing.out","w",stdout);
    int N;
    cin>>N;
    vii speedlimit;
    vii driving;
    char c;
    int step;
    char b[5];
    int pre=0;
    char M[3][3];
    map<pair<int,int>,int> um;
    int ans=2000;
    int x=0;
    int y=0;
    int k=0;
    um[make_pair(0,0)]=0;
    for(int i=0;i<N;i++)
    {
        cin>>c>>step;
        int xx=0;
        int yy=0;
        if(c=='N')
            yy=1;
        else if (c=='S')
            yy=-1;
        else if (c=='E')
            xx=1;
        else
            xx=-1;
        for(int j=0;j<step;j++)
        {
            x+=xx;
            y+=yy;
            k+=1;
            if(um.count(make_pair(x,y))>0)
            {
                ans=min(ans,k-um[make_pair(x,y)]);
               // cout<<um[make_pair(x,y)]<<"-"<<x<<":"<<y<<endl;
            }
            //cout<<k<<"=="<<x<<":"<<y<<"k"<<k<<endl;
            um[make_pair(x,y)]=k;
            
        }

    }
    if(ans==2000)
    ans=-1;
   cout<<ans<<endl;
}