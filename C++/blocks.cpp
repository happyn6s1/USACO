#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define vii vector<pair<int,int>> 
int main()
{
    freopen("blocks.in","r",stdin);
    freopen("blocks.out","w",stdout);
    int N,M;
    cin>>N;
    vii speedlimit;
    vii driving;
    string a,b;
    int pre=0;
    int ll[26]={0};
    for(int i=0;i<N;i++)
    {
        cin>>a>>b;
        int la[26]={0};
        int lb[26]={0};
        for(char c:a)
        {
            la[c-'a']+=1;
        }
        for(char c:b)
        {
            lb[c-'a']+=1;
        }
        for(int i=0;i<26;i++)
        {
            ll[i]+=max(la[i],lb[i]);
        }
    }
    for(int i=0;i<26;i++)
    {
        cout<<ll[i]<<endl;
    }

}