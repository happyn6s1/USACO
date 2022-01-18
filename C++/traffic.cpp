#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define vvi vector<vector<int>> 
int main()
{
    freopen("traffic.in","r",stdin);
    freopen("traffic.out","w",stdout);
    int N,M;
    cin>>N;
    vvi p;
    string s;
    int a,b,c,k;
    int pre=0;
    for(int i=0;i<N;i++)
    {
        cin>>s>>a>>b;
        if(s=="on")
        {
            k=1;
        }
        else if(s=="off")
        {
            k=-1;
        }
        else
        {
            k=0;
            c=i;
        }
        p.push_back({i,k,a,b});
        
    }
    int aa,bb;
    //int k=0;
    aa=1000;
    bb=0;
        bool F;
        int m0,m1,j;
         F=true;
         vector<int> v;
        m0=-9999;
        m1=9999;
        for(j=p.size()-1;j>-1;j--)
        {
            v=p[j];
            if(v[1]==0)
            {
                m0=max(m0,v[2]);
                m1=min(m1,v[3]);
            }
            else if(v[1]==1)
            {
                m0-=v[3];
                m1-=v[2];
            }
            else{
                m1+=v[3];
                m0+=v[2];
            }
        }
        cout<<max(0,m0)<<" "<<m1<<endl;

        m0=-9999;
        m1=9999;
        for(auto v:p)
        {
            if(v[1]==0)
            {
                m0=max(m0,v[2]);
                m1=min(m1,v[3]);
            }
            else if(v[1]==-1)
            {
                m0-=v[3];
                m1-=v[2];
            }
            else{
                m1+=v[3];
                m0+=v[2];
            }
        }
        cout<<max(0,m0)<<" "<<m1<<endl;
   
}