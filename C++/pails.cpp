#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define vii vector<pair<int,int>> 
int main()
{
    freopen("pails.in","r",stdin);
    freopen("pails.out","w",stdout);
    int X,Y,M;
    cin>>X>>Y>>M;
    int ans=0;
    for(int i=0;i<M/X;i++)
    {
        int r=(M-i*X-X)%Y;
        ans=max(ans,M-r);
    }
    cout<<ans;
       //cout<<endl<<vcc.size();
}