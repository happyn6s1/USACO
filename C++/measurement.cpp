#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define vii vector<pair<int,int>> 
int main()
{
    freopen("measurement.in","r",stdin);
    freopen("measurement.out","w",stdout);
    int N;
    cin>>N;
    int day;
    string name;
    int idd;
    string change;
    vector<vector<int>> vvx;
    for(auto i=0;i<N;i++)
    {
        cin>>day>>name>>change;
        if(name=="Mildred")
        {
            idd=0;
        }
        else if(name=="Elsie")
            idd=1;
        else
            idd=2;
        int c=stoi(change);
        vvx.push_back({day,idd,c});
        //cout<<day<<id<<c<<endl;
    }
    sort(vvx.begin(),vvx.end());
    int d[3]={7,7,7};
    int x=7;
    int ans=0;
    for(vector<int> v:vvx)
    {
        d[v[1]]+=v[2];
        int k=0;
        //cout<<d[0]<<" "<<d[1]<<" "<<d[2]<<endl;
        if(d[0]>=d[1] and d[0]>=d[2])
            k+=1;
        if(d[1]>=d[0] and d[1]>=d[2])
            k+=2;
        if(d[2]>=d[1] and d[2]>=d[0])
            k+=4;
        if(k!=x)
          ans+=1;
        x=k;
    
            
    }
    cout<<ans;
}