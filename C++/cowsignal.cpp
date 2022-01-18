#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main()
{
    freopen("cowsignal.in","r",stdin);
    freopen("cowsignal.out","w",stdout);
    int M,N,K;
    cin>>M>>N>>K;
    for(int i=0;i<M;i++)
    {
        vector<char> vc;
        string s;
        cin>>s;
        for(int j=0;j<N;j++)
        {
            for(int k=0;k<K;k++)
            {
                vc.push_back(s[j]);
            }
        }
        for(int k=0;k<K;k++)
        {
            for(int j=0;j<K*N;j++)
                cout<<vc[j];
            cout<<endl;
        }
        
    }
}