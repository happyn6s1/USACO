#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define vii vector<pair<int,int>> 
int main()
{
    freopen("gymnastics.in","r",stdin);
    freopen("gymnastics.out","w",stdout);
    int N,K;
    cin>>K>>N;
    int ans=0,a;
    vector<vector<int>> position;
    for(int i=0;i<K;i++)
        {
            vector<int> tmp;
        for(int j=0;j<N;j++)
        {
            tmp.push_back(0);
        }
        position.push_back(tmp);
        }
    for(int i=0;i<K;i++)
    {
        
        for(int j=0;j<N;j++)
        {
            cin>>a;
            a-=1;
            position[i][a]=j;
        }
    }
    
    for(int i=0;i<N;i++)
        for(int j=0;j<N;j++)
            {
                if(i==j)
                   continue;
                bool F=true;

            for(int k=0;k<K;k++)
            {
                if(position[k][i]<position[k][j]){
                    F=false;
                    break;
                }
            } 
            //cout<<i<<" "<<j<<" "<<F<<endl;
            if(F)
                ans+=1;
            }       
    cout<<ans;
       //cout<<endl<<vcc.size();
}