#include <bits/stdc++.h>
#include <iostream>
#include <queue>
using namespace std;
    int N,T,K;
#define vii vector<pair<int,int>> 
    char result[8][8];
    char A[8][8];
    char B[8][8];
    bool possible[100];
//bool M[7][7]={false};   
int nos=0;
string s;
/*
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
set<int> possiblev;
void backtrack(int i, vector<int> a, vector<int>b,int  m,int n)
{
    //cout<<i<<"=="<<m<<n<<endl;
    if(i==4){
        possiblev.insert(m);
    //cout<<m<<endl;
    return;
    }
    if(i%2==0)
    {
        for(int j=0;j<a.size();j++)
        {
            vector<int> tta,ttb;
            tta=a;
            ttb=b;
            //cout<<"here"<<endl;
            tta.erase(tta.begin()+j);
            ttb.push_back(a[j]);
            backtrack(i+1,tta,ttb,m-a[j],n+a[j]);
        }
    }  
    else
    {
        for(int j=0;j<b.size();j++)
        {
            vector<int> tta,ttb;
            ttb=b;
            tta=a;
            ttb.erase(ttb.begin()+j);
            tta.push_back(b[j]);
            backtrack(i+1,tta,ttb,m+b[j],n-b[j]);
        }
    }  
    
}*/
    bool M[10][10];
int total=0;
void flip(int i,int j)
{
    total+=1;
    //cout<<i<<" and "<<j<<endl;
    for(int ii=0;ii<i;ii++)
    for(int jj=0;jj<j;jj++)
        M[ii][jj]= not M[ii][jj];
}
int  recur(int i)
{
    int j=i;
    if(j==1)
        return j;
    else{
        j=j*recur(i+1);
    }
    cout<<j;
    return j;
}
 int modu(int a, int b, int n){
    long long x=1, y=a; 
    while (b > 0) {
        if (b%2 == 1) {
            x = (x*y) % n; // multiplying with base
        }
        y = (y*y) % n; // squaring the base
        b /= 2;
    }
    return x % n;
}
int  pp[26][1501];
int longest(string s, char c, int k)
{
    //int k=sset.size();
    int n=0;
    int slow=0;
    int fast=0;
    int ans=0;
    while(fast<s.length())
    {
        //cout<<s<<endl;
        if(s[fast]!=c)
            n+=1;
        //cout<<n<<k<<fast<<endl;
        if(n==k+1)
        {

            n-=1;
            break;
        }
        fast+=1;
    }
    ans=fast-slow;
    //cout<<ans<<"=k="<<k<<"-fast-"<<fast<<"-slow-"<<slow<<n<<endl;
    for(slow=1;slow<s.size();slow++)
    {
        if(s[slow-1]!=c)
        {
            n-=1;
            while(fast<s.length())
            {
                if(s[fast]!=c)
                {
                    n+=1;
                    if(n==k+1)
                    {   n-=1;
                        break;
                    }
                }
                fast+=1;
            }
        }
        
        ans=max(ans,fast-slow);
        
    }
    //cout<<ans<<endl;
    return ans;
}
const int X=501;
long long grid[X][X];
bool visited[X][X];
long long dist[X][X];
bool adj[X][X];
int row_num;
int col_num;
int cur_size=0;
int cur_border=0;
//bool visited[X];
/*void dfs(int node)
{
	visited[node] = true;
	for(int u:adj[node])
		if(!visited[u])
			dfs(u);
}
*/
long long mid;
void ff(int x,int y)
{
    if((x<0 || y<0 or x>=row_num or y>=col_num ) or visited[x][y])
        return;
    visited[x][y]=true;
    cur_size++;
    
    if(y+1<col_num and abs(grid[x][y]-grid[x][y+1])<=mid)
        ff(x,y+1);
    if(y-1>=0 and abs(grid[x][y]-grid[x][y-1])<=mid)
    ff(x,y-1);
    if(x+1<row_num and abs(grid[x][y]-grid[x+1][y])<=mid)
    ff(x+1,y);
    if(x-1>=0 and abs(grid[x][y]-grid[x-1][y])<=mid)
    ff(x-1,y);
    //cout<<x<<":"<<y<<cur_size<<cur_border<<endl;
    
}

int main()
{
    //freopen("ccski.in","r",stdin);
    //freopen("ccski.out","w",stdout);
    //vector<long long> a;
    //v<int> b;
    //cout<<"hell"<<endl;
    //cout<<recur(5);
    //return 0;
    long long  t,a,b,d;
    char c;
    int N,M,B,Q;
    long long K;
    string s;
    
    //int l[101];
    //cout<<"help"<<N<<Q<<endl;
    
    vector<pair<int, int>> p;
    //vector<vector<int>> g; //graph
    vector<long long> l;
    vector<long long> ll;
    vector<long long> tower;

    cin>>N>>M; //city and road
    //M=N;
    row_num=N;
    col_num=M;
    vector<vector<int>> g; //graph
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<M;j++)
        {
            cin>>a;
            grid[i][j]=a;
        }
    }
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<M;j++)
        {
            cin>>a;
            if(a==1)
            p.push_back(make_pair(i,j));
        }
    }
    if(p.size()<=1)
    {
        cout<<0;
        return 0;
    }
    set<pair<int,int>> ps;
    for(int i=1;i<p.size();i++)
    {
        ps.insert(p[i]);
    }
    int lo=0;
    int hi=1000000000;
    int ans=hi;
    int size=0;
    while(lo<=hi)
    {   
                for(int i=0;i<N;i++)
    
        for(int j=0;j<M;j++)
         visited[i][j]=false;

        bool F=true;
        mid=(lo+hi)/2;
        ff(p[0].first,p[0].second);
        for(int i=1;i<p.size();i++)
        {

            if(not visited[p[i].first][p[i].second])
            {
                F=false;
                break;
            }
        }
        if(F)
        {
            ans=mid;
            hi=mid-1;
        }
        else
        {
            lo=mid+1;
        }

    }
    cout<<ans;
        //check connected
    
    
 }