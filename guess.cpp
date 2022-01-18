#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define vii vector<pair<int,int>> 
int main()
{
    freopen("guess.in","r",stdin);
    freopen("guess.out","w",stdout);
    int N;
    string s;
    cin>>N;
    vector<set<string>> chr;

    for(int i=0;i<N;i++)
    {
        int n;
        cin>>s>>n;
        set<string> temp;
        chr.push_back(temp);
        for(int j=0;j<n;j++)
        {
            cin>>s;
            chr.back().insert(s);
        }
        //cout<<chr.back().size()<<endl;
    }
    int ans=0;
    for(int i=0;i<N;i++)
        for(int j=i+1;j<N;j++)
        {
            vector<string> temp;
            set<string> s1,s2,s3;
            s1=chr[i];
            s2=chr[j];
            set_intersection(s1.begin(),s1.end(),s2.begin(),s2.end(), back_inserter(temp));
            //cout<<temp.size()<<endl;  
            ans=max(ans,(int)temp.size());
        }
   cout<<ans+1;

       //cout<<endl<<vcc.size();
}