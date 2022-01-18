#include <bits/stdc++.h>
#include <iostream>
using namespace std;
    int N,T,K;
#define vii vector<pair<int,int>> 
    char result[8][8];
    char A[8][8];
    char B[8][8];
    bool possible[100];
   

int main()
{
    //freopen("bcs.in","r",stdin);
    //freopen("bcs.out","w",stdout);

    cin>>N;
    long long apple[20];
    for(int i=0;i<N;i++)
        cin>>apple[i];
    long long s=0;
    for(int i=0;i<N;i++)
        s+=apple[i];
    
    long ans=s;
    for(long long i=0;i<pow(2,N);i++)
    {
        long long t=0;
        long long j=i;
        for(int k=0;k<N;k++)
        {
            if(j%2)
                t+=apple[k];
            j=j/2;
        }
        if (abs(2*t-s)<ans)
            ans=abs(2*t-s);

    }
    cout<<ans;      //cout<<endl<<vcc.size();
}