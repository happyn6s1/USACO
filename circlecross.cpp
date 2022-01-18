#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define vii vector<pair<int,int>> 
int main()
{
    freopen("circlecross.in","r",stdin);
    freopen("circlecross.out","w",stdout);
    int N;
    string s;
    cin>>s;
    int M[26][2];
    for(int i=0;i<26;i++)
    {
        M[i][0]=-1;
        M[i][1]=-1;
    }
    for(int i=0;i<52;i++)
    {
        int c=s[i]-'A';
        if(M[c][0]>-1)
        {
            M[c][1]=i;
        }
        else
        M[c][0]=i;

    }
    int ans=0;
    for(int i=0;i<26;i++)
    for(int j=i+1;j<26;j++)
    {
        int a,b,c,d;
        a=M[i][0];
        b=M[i][1];
        c=M[j][0];
        d=M[j][1];
        if ((c-a)*(c-b)<0 and (d-a)*(d-b)>0 or (c-a)*(c-b)>0 and (d-a)*(d-b) < 0)
        {//cout<<i<<" "<<j<<endl;
            ans+=1;
        }
    }
    cout<<ans;

       //cout<<endl<<vcc.size();
}