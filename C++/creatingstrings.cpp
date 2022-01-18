#include <bits/stdc++.h>
#include <iostream>
using namespace std;
    int N,T,K;
#define vii vector<pair<int,int>> 
    char result[8][8];
    char A[8][8];
    char B[8][8];
    bool possible[100];
   
vector<string> perm(vector<char> l)
{
    vector<string> ans;
    if(l.size()==0)
    {
        ans.push_back("");
        return ans;
    }
    set<char> s;
    for(char c:l)
    {s.insert(c);}
    //sort(s.begin(),s.end());

    for(char c:s)
    {
        string ss(1,c);
        //cout<<ss<<endl;
        bool F=false;
        vector<char> t;
        for(char cc:l)
        {
            if(c==cc and not F)
            {F=true;
            }
            else
            {
                t.push_back(cc);
            }
        }
        vector<string> ttt=perm(t);
        for(string ts:ttt)
            ans.push_back(ss+ts);

    }
    //cout<<ans.size()<<" "<<l.size()<<endl;
    return ans;

}
int main()
{
    //freopen("bcs.in","r",stdin);
    //freopen("bcs.out","w",stdout);

    string s;
    cin>>s;
    N=s.length();
    vector<char> clist;
    for(int i=0;i<N;i++)
        clist.push_back(s[i]);
    vector<string> ans;
    ans=perm(clist);
    cout<<ans.size()<<endl;
    for(string a:ans)
        cout<<a<<endl;      //cout<<endl<<vcc.size();
}