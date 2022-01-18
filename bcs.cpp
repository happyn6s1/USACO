#include <bits/stdc++.h>
#include <iostream>
using namespace std;
    int N,T,K;
#define vii vector<pair<int,int>> 
    bool result[100];
    bool possible[100];
    vector<vector<int>> timet;
    bool check(int ii, int j)
    {
        int p[100];
        for(int i=0;i<N;i++)
            p[i]=-1;
        p[ii]=0;
        for(vector<int> v:timet)
        {
            int x=v[1];
            int y=v[2];
            int t=v[0];
            //cout<<x<<" : "<<y<<" : "<<t<<endl;
 
            
            if(p[x]>-1 and p[y]==-1 and p[x]<j){
                p[x]+=1;
                    p[y]=0;
                //p[x]+=1;
            }
        
            
            else if(p[y]>-1 and p[x]==-1 and p[y]<j)
             {       p[x]=0; p[y]+=1;
             }  
            
            else if (p[x]>-1 and p[y]>-1)
             {
               
            p[x]+=1;
                p[y]+=1;
             }
            //if(ii==3)
            //cout<<p[0]<<p[1]<<p[2]<<p[3]<<p[4]<<":"<<ii<<":"<<j<<"try"<<endl;
        }   
        bool ans=true;

        for(int i=0;i<N;i++)
        {
            if(result[i] and p[i]==-1 or (not result[i] and p[i]>-1))
            {
                //if(ii==0)
                //cout<<i<<j<<result[i]<<p[i]<<endl;
                ans=false;
                break;
            } 
        } 
        //cout<<p[0]<<p[1]<<p[2]<<p[3]<<p[4]<<":"<<ii<<":"<<j<<"ans"<<ans<<endl;
        //cout<<result[0]<<result[1]<<result[2]<<result[3]<<result[4]<<":"<<ii<<":"<<j<<endl;
        return ans;
    }
int main()
{
    freopen("bcs.in","r",stdin);
    freopen("bcs.out","w",stdout);

    cin>>N>>K;
    //vector<pair<int,int>> pos;
    //vector<int> XX;
    //vector<int> YY;

    string s;
    cin>>s;
    for(int i=0;i<N;i++)
    {
        if(s[i]=='1')
            result[i]=true;
        else
            result[i]=false;    
        possible[i]=false;
    }
    //vector<vector<int>> time;
    for(int i=0;i<T;i++)
    {
        int a,b,c;
        cin>>a>>b>>c;
        timet.push_back({a,b-1,c-1});
    }
    int ans=0;
    sort(timet.begin(),timet.end());
    int y=251,z=-1;
    
    
    for(int i=0;i<N;i++)
    {
            for(int j=0;j<251;j++)
        {
            if(check(i,j))
            {
                //cout<<i<<j<<endl;
                possible[i]=true;
                y=min(y,j);
                z=max(z,j);
            }
        }
        if(possible[i])ans+=1;
    }
    cout<<ans<<" "<<y<<" ";
    if(z==250)
    cout<<"Infinity";
    else
    cout<<z;
       //cout<<endl<<vcc.size();
}