#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define vii vector<pair<int,int>> 
int main()
{
    freopen("balancing.in","r",stdin);
    freopen("balancing.out","w",stdout);
    int N,B;
    cin>>N>>B;
    vector<pair<int,int>> pos;
    vector<int> XX;
    vector<int> YY;
          
    int ans=0,a,b;
    for(int i=0;i<N;i++)
        {
            string s;
            cin>>a>>b;
            pos.push_back(make_pair(a,b));
            XX.push_back(a);
            YY.push_back(b);
                
        }
    sort(XX.begin(),XX.end());
    sort(YY.begin(),YY.end());
    vector<int> X={0};
    vector<int> Y={0};
    for(int i=1;i<XX.size();i++)
    {
        if(XX[i]>XX[i-1])
            X.push_back(XX[i]-1);

    }
    for(int i=1;i<YY.size();i++)
    {
        if(YY[i]>YY[i-1])
            Y.push_back(YY[i]-1);
            
    }
    ans=pos.size();
    for(int p:X)
    for(int q:Y)
    {
        int a=0;
        int b=0;
        int c=0;
        int d=0;
        for(pair<int,int> pp:pos)
        {
            int x=pp.first;
            int y=pp.second;
            if( x > p and y>q)
                a+=1;
            else if(x>p and y<q)
                b+=1;
            else if(x<p and y<q)
                c+=1;
            else if(x<p and y>q)
                d+=1;
        }        

        ans=min(ans,max(max(a,b),max(c,d)));
    }
    cout<<ans;
       //cout<<endl<<vcc.size();
}