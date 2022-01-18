#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define vii vector<pair<int,int>> 
int main()
{
    freopen("cownomics.in","r",stdin);
    freopen("cownomics.out","w",stdout);
    int N,M;
    cin>>N>>M;
    vector<bool> spot[4];
    vector<bool> plain[4];
    for(int i=0;i<4;i++)
        for(int j=0;j<M;j++){
            spot[i].push_back(false);
            plain[i].push_back(false);
        }   
    int ans=0,a;
    for(int i=0;i<N;i++)
        {
            string s;
            cin>>s;
            for(int j=0;j<M;j++)
            {
                if(s[j]=='A')
                    spot[0][j]=true;
                else if(s[j]=='C')
                    spot[1][j]=true;
                else if(s[j]=='G')
                    spot[2][j]=true;
                else if(s[j]=='T')
                    spot[3][j]=true;
            }
        }
    for(int i=0;i<N;i++)
        {
            string s;
            cin>>s;
            for(int j=0;j<M;j++)
            {
                if(s[j]=='A')
                    plain[0][j]=true;
                else if(s[j]=='C')
                    plain[1][j]=true;
                else if(s[j]=='G')
                    plain[2][j]=true;
                else if(s[j]=='T')
                    plain[3][j]=true;
            }
        }
    for(int i=0;i<M;i++)
    {
        bool F=true;
        for(int j=0;j<4;j++)
        {
            if(spot[j][i] and plain[j][i])
            {F=false;break;}
        }
        if(F)
        ans+=1;
    }
   cout<<ans;
       //cout<<endl<<vcc.size();
}