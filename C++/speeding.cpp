#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define vii vector<pair<int,int>> 
int main()
{
    freopen("speeding.in","r",stdin);
    freopen("speeding.out","w",stdout);
    int N,M;
    cin>>N>>M;
    vii speedlimit;
    vii driving;
    int a,b;
    int pre=0;
    for(int i=0;i<N;i++)
    {
        cin>>a>>b;
        if(i>0)
            a+=speedlimit[i-1].first;
        speedlimit.push_back(make_pair(a,b));
        
    }
    int j=0;
    int ans=0;
    int p=0;
    for(int i=0;i<M;i++)
    {
        cin>>a>>b;
        if(i>0)
            a=a+driving[i-1].first;
        //cout<<"aaa"<<speedlimit[j].first<<driving[i-1].first<<endl;
        driving.push_back(make_pair(a,b));
    }
    for(pair<int,int> pp:speedlimit)
    {
        while (j<driving.size()-1 and driving[j].first<pp.first)
        {
            ans=max(ans,driving[j].second-pp.second);
            cout<<ans<<" "<<driving[j].second<<"-"<<pp.second<<endl;
            j+=1;
        }
        cout<<ans<<" :"<<driving[j].second<<"-"<<pp.second<<endl;
        ans=max(ans,driving[j].second-pp.second);
    }
    //cout<<"what";
    cout<<ans;



}