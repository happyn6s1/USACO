#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define vvi vector<vector<int>> 
#define vi vector<int>
int main()
{
    freopen("cbarn.in","r",stdin);
    freopen("cbarn.out","w",stdout);
    int N,M;
    cin>>N;
    vi p;
    string s;
    int a,b,c,k;
    long long pre=0;
    for(int i=0;i<N;i++)
    {
        cin>>a;
        p.push_back(a);
        
    }
    long long ans=99999999;
    c=p.size();
    for(b=0;b<c;b++)
    {
        pre=0;
        for(int j=0;j<c;j++)
        {
            pre+=p[(b+j)%c]*j;
        }
        ans=min(ans,pre);
    }
    cout<<ans;
  
}