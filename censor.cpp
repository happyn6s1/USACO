#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define vii vector<pair<int,int>> 
int main()
{
    freopen("censor.in","r",stdin);
    freopen("censor.out","w",stdout);
    int N;
    //cin>>N;
    vii speedlimit;
    vii driving;
    char c;
    int step;
    char b[5];
    int pre=0;
    char M[3][3];
    int ans=2000;
    long long x=0;
    int y=0;
    int k=0;
    string s;
    string t;
    stack<char> sc;
    stack<long> mv;
    cin>>s;
    cin>>t;
    x=t.length();
    mv.push(-1);
    for(char c:s)
    {
        sc.push(c);
        //y=mv.top();
        bool F=false;
        //y+=1;
        //if(c==t[y])
        //{
        //    if(y==x-1)
        //        F=true;
        //}
        
        //else if(c==t[0])
        //{
        //    y=0;
        //}
        //else
        //    y=-1;
       // cout<<y<<F<<"x"<<x<<endl;
        //mv.push(y);
        if(sc.size()>=x)
        {
            stack<char> temp;
            int i;
            for(i=0;i<x;i++)
            {
                if(sc.top()!=t[x-1-i])
                {F=false;
                while(temp.size()>0)
                {
                    sc.push(temp.top());
                    temp.pop();
                }
                break;}
                temp.push(sc.top());
                sc.pop();
            }
        }
//        if(F)
  //      {
    //        for(auto i=0;i<x;i++)
      //      {
        //        sc.pop();
          //     mv.pop();
            //}
        //}
       // cout<<mv.back()<<endl;
    }
    vector<char> vcc;
    while(sc.size()>0)
    {
     vcc.push_back(sc.top());
    sc.pop();
    }
    for(long long j=vcc.size()-1;j>-1;j--)
    {
        cout<<vcc[j];
    }
    //cout<<endl<<vcc.size();
}