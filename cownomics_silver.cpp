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
    char S[500][50];
    char P[500][50];
      
    int ans=0,a;
    for(int i=0;i<N;i++)
        {
            string s;
            cin>>s;
            for(int j=0;j<M;j++)
                S[i][j]=s[j];
                
        }
    for(int i=0;i<N;i++)
        {
            string s;
            cin>>s;
            for(int j=0;j<M;j++)
                P[i][j]=s[j];
                
        }
    for(int i=0;i<M;i++)
    for(int j=i+1;j<M;j++)
    for(int k=j+1;k<M;k++)
    {
        unordered_set<string> set1,set2;
        //cout<<"what";
        for(int p=0;p<N;p++)
        {
            //string s1,s2;
            char p1[4];
           // char p2[4];
            p1[3]=0;
           // p2[3]=0;
            p1[0]=S[p][i];
           // p2[0]=P[p][i];
            p1[1]=S[p][j];
           // p2[1]=P[p][j];
            p1[2]=S[p][k];
           // p2[2]=P[p][k];
           //  cout<<s1<<s2<<S[p][i]<<endl;
            set1.insert(p1);
          //  set2.insert(p2);
            
        }

        bool F=true;
        for(int p=0;p<N;p++)
        {
            //string s1,s2;
            //char p1[4];
            char p2[4];
            //p1[3]=0;
            p2[3]=0;
           // p1[0]=S[p][i];
            p2[0]=P[p][i];
           // p1[1]=S[p][j];
            p2[1]=P[p][j];
           // p1[2]=S[p][k];
            p2[2]=P[p][k];
           //  cout<<s1<<s2<<S[p][i]<<endl;
            

            if(set1.count(p2)>0){
               // cout<<t.second<<endl;
                F=false;
                break;
            }
        }
        if(F)
            ans+=1;
    }
    //ans+=1;
    
    cout<<ans;
       //cout<<endl<<vcc.size();
}