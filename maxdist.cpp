#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define vii vector<pair<int,int>> 
int main()
{
    //freopen("censor.in","r",stdin);
    //freopen("censor.out","w",stdout);
    int N,a;
    cin>>N;
    long long ans=0;
    vector<pair<int,int>> l;
    for(int i=0;i<N;i++)
    {

        cin>>a;
        l.push_back(make_pair(a,0));
    }
    for(int i=0;i<N;i++)
    {

        cin>>a;
        l[i].second=a;
    }
    for(int i=0;i<N;i++)
        for(int j=i+1;j<N;j++)
        {
            ans=max(ans,(long long)(l[i].first-l[j].first)*(l[i].first-l[j].first)+(l[i].second-l[j].second)*(l[i].second-l[j].second));
        }
    cout<<ans;
       //cout<<endl<<vcc.size();
}