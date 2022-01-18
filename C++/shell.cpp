#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main()
{
    freopen("shell.in","r",stdin);
    freopen("shell.out","w",stdout);
    //int r1=0,r2=0,r3=0;
    //int c1=1,c2=2,c3=3;
    vector<int> r={0,0,0};
    vector<int> cc={1,2,3};
    int n,a,b,c;
    
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>a>>b>>c;
        for(int j=0;j<n;j++)
        {
            if(a==cc[j])
                cc[j]=b;
            else if(b==cc[j])
                cc[j]=a;
            if(cc[j]==c)
                r[j]+=1;
        }
        /*
        if(a==c1)
            c1=b;
        else if(b==c1)
            c1=a;
        if(a==c2)
            c2=b;
        else if(b==c2)
            c2=a;
        if(a==c3)
            c3=b;
        else if(b==c3)
            c3=a;
        if(c1==c)
            r1+=1;
        if(c2==c)
            r2+=1;
        if(c3==c)
            r3+=1;
        //cout<<c1<<c2<<c3<<c<<r1<<r2<<r3<<endl;    
        */

    }
    //cout<<max(r[0],max(r[1],r[2]));  

    cout<<*std::max_element(r.begin(),r.end());  

}