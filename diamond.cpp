#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define vii vector<pair<int,int>> 
int main()
{
    freopen("diamond.in","r",stdin);
    freopen("diamond.out","w",stdout);
    int N,K;
    cin>>N>>K;
    int ans=0,a;
    vector<int> vv;
    for(int i=0;i<N;i++)
    {
        cin>>a;
        vv.push_back(a);
    }
    sort(vv.begin(),vv.end());
    for(int i=0;i<N;i++)
        {
        for(int j=i;j<N;j++)
            {if(vv[j]-vv[i]>K)
                break;
            //cout<<j<<" "<<i<<vv[j]<<" "<<vv[i]<<endl;
            ans=max(ans,j-i+1);
            } 
        }
    cout<<ans;
       //cout<<endl<<vcc.size();
}