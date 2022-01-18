#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main()
{
    freopen("mixmilk.in","r",stdin);
    freopen("mixmilk.out","w",stdout);
    //int r1=0,r2=0,r3=0;
    //int c1=1,c2=2,c3=3;
    vector<int> r={0,0,0};
    vector<int> c={1,2,3};
    for(int i=0;i<3;i++)
        cin>>c[i]>>r[i];
    for(int i=0;i<100;i++)
    {
        int x=i%3;
        int y=(i+1)%3;
        if(r[x]+r[y]<=c[y])
        {

           
            r[y]+=r[x];
            r[x]=0;
        }
        else
        {
            r[x]=r[x]+r[y]-c[y];
            r[y]=c[y];
            
        }

    }
    for(int i=0;i<3;i++)
        cout<<r[i]<<endl;

}