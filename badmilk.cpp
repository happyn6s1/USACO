#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define vii vector<pair<int,int>> 
int main()
{
    freopen("badmilk.in","r",stdin);
    freopen("badmilk.out","w",stdout);
    int N,M,D,S;
    cin>>N>>M>>D>>S;
    //vector<pair<int,int>> pos;
    //vector<int> XX;
    //vector<int> YY;
    bool tab[50][50];
    for(int i=0;i<50;i++)
    for(int j=0;j<50;j++)
    {
        tab[i][j]=true;
    }    
    vector<vector<int>> drink;
    int ans=0,a,b,c;
    for(int i=0;i<D;i++)
    {
        cin>>a>>b>>c;
        drink.push_back({a-1,b-1,c});

    }
    int sickday[50];
    for(int j=0;j<50;j++)
    {
        sickday[j]=-1;
    }    

    for(int i=0;i<S;i++)
    {
        cin>>a>>b;
        a=a-1;
        sickday[a]=b;
        for(int j=0;j<M;j++)
        tab[a][j]=false;
    }
    for(vector<int> v:drink)
    {
        if(sickday[v[0]]>-1 and v[2]<sickday[v[0]])
            tab[v[0]][v[1]]=true;
    }
    vector<int> poison;
    for(int i=0;i<M;i++)
    {
        bool F=true;
        for(int j=0;j<N;j++)
        {
            //cout<<tab[0][1]<<":"<<i<<"asd"<<j<<"dfd"<<tab[j][i]<<endl;
            F=F and tab[j][i];
            }
        if(F)
            poison.push_back(i);

    }
   
    for(int i=0;i<poison.size();i++)
    {
         set<int> sickp;
        for(vector<int> v:drink)
        {   
           // cout<<poison[i]<<"as"<<v[1]<<endl;
            if(v[1]==poison[i])
             sickp.insert(v[0]);           
        }
        ans=max(ans,(int)sickp.size());
    }
   cout<<ans;
       //cout<<endl<<vcc.size();
}