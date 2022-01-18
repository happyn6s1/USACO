#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define vii vector<pair<int,int>> 
int main()
{
    //freopen("diamond.in","r",stdin);
    //freopen("diamond.out","w",stdout);
    int N,K;
    cin>>N;
    int ans=0,a;
    vector<int> pre={0};
    vector<int> vv;
    for(int i=0;i<N;i++)
    {
        cin>>a;
        vv.push_back(a);
        pre.push_back(pre.back()+a);
    }
    
    for(int i=0;i<N;i++)
        for(int j=i;j<N;j++)

            {
                int s=pre[j+1]-pre[i];
                for(int k=i;k<j+1;k++)
                {
                    if(vv[k]*(j-i+1)==s){
                        ans+=1;
                        break;
                    }
                }
            } 
        
    cout<<ans;
       //cout<<endl<<vcc.size();
}