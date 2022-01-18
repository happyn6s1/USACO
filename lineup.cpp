#include <bits/stdc++.h>
#include <iostream>
using namespace std;
    int N,T,K;
#define vii vector<pair<int,int>> 
    char result[8][8];
    char A[8][8];
    char B[8][8];
    bool possible[100];
bool M[7][7]={false};   
int nos=0;
string s;

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
bool isgood(int n,int j)
{
    bool F=true;
    
    for(int i=0;i<8;i++)
    {
        if(M[i][j]=='#' and i!=n)
        return false;
        
    }
    for (int i=1;i<8;i++)
    {
        if(n+i<8 and j+i<8 and M[n+i][j+i]=='#')
            return false;
    }
    for (int i=1;i<8;i++)
    {
        if(n+i<8 and j-i>=0 and M[n+i][j-i]=='#')
            return false;
    }
    for (int i=1;i<8;i++)
    {
        if(n-i>=0 and j+i<8 and M[n-i][j+i]=='#')
            return false;
    }
    for (int i=1;i<8;i++)
    {
        if(n-i>=0 and j-i>=0 and M[n-i][j-i]=='#')
            return false;
    }
    return true;
}
void backtrack(int n,int i, int j)
{
    //cout<<n<<endl;
    if(n==48)
    {
        if (i==6 and j==0)
            nos+=1;
        //cout<<nos<<endl;
        return;
    }

    if((s[n]=='?' or s[n]=='L' ) and j>0 and not M[i][j-1])
    {
        M[i][j-1]=true;
        backtrack(n+1,i,j-1);
        M[i][j-1]=false;
        
    }
    if((s[n]=='?' or s[n]=='U') and i>0 and not M[i-1][j])
    {
        M[i-1][j]=true;
        backtrack(n+1,i-1,j);
        M[i-1][j]=false;
        
    }
    if((s[n]=='?' or s[n]=='R' )and j+1<=6 and not M[i][j+1])
    {
        M[i][j+1]=true;
        backtrack(n+1,i,j+1);
        M[i][j+1]=false;
        
    }
    if((s[n]=='?' or s[n]=='D' )and i+1<=6 and not M[i+1][j])
    {
        M[i+1][j]=true;
        backtrack(n+1,i+1,j);
        M[i+1][j]=false;
        
    }
}
int main()
{
    freopen("lineup.in","r",stdin);
    freopen("lineup.out","w",stdout);
    map<string,int> mapcow;
    mapcow["Beatrice"]=0;
    mapcow["Belinda"]=1;
    mapcow["Bella"]=2;
    mapcow["Bessie"]=3;
    mapcow["Betsy"]=4;
    mapcow["Blue"]=5;
    mapcow["Buttercup"]=6;
    mapcow["Sue"]=7;
    string cow[8]={"Beatrice","Belinda","Bella","Bessie","Betsy","Blue","Buttercup","Sue"};
    int N;
    cin>>N;
    vector<int> edgelist[8];
    int degree[8]={0};
    bool visited[8]={false};
    for(int i=0;i<N;i++)
    {

        string a,b,s;
        cin>>a;
        cin>>b;
        cin>>b;
        cin>>b;
        cin>>b;
        cin>>b;
        int ai=mapcow[a];
        int bi=mapcow[b];
        edgelist[ai].push_back(bi);
        edgelist[bi].push_back(ai);
        degree[ai]+=1;
        degree[bi]+=1;
        
    }    
    vector<int> ans;
    priority_queue<int> g;
    stack<int> sti;
    for(int i=0;i<8;i++)
    {
        if(visited[i] or degree[i]>1)
        continue;
        //cout<<i<<"aaa"<<endl;
        sti.push(i);
        while(!sti.empty())
        {
            int t=sti.top();
            sti.pop();
            visited[t]=true;
            ans.push_back(t);
            for(int j:edgelist[t])
            {
                if(not visited[j])
                {
                    sti.push(j);
                }
            }
        }
    }
    for(int k:ans)
        cout<<cow[k]<<endl;
}