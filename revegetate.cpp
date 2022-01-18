#include <bits/stdc++.h>
#include <iostream>
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
int main()
{
    freopen("revegetate.in","r",stdin);
    freopen("revegetate.out","w",stdout);
    //vector<long long> a;
    //v<int> b;

    int  t,tt,a,b;
    int K,N,M;
    vector<int> l[101];
    vector<int> g;
    cin>>N>>M;
    string A,B;
    long long  ans=0;
    t=0;
    a=0;
    b=0;    
    //int degree[100001]={0};
    long long k;
    for(int i=0;i<M;i++)
    {
        cin>>a>>b;
        l[a].push_back(b);
        l[b].push_back(a);
        //cout<<t<<endl;
    }
    int color[101];
    for(int i=1;i<N+1;i++)
    {
        bool flag[4]={true,true,true,true};
        for(int j:l[i])
        {
            //cout<<i<<" : "<<j<<endl;
            if(j<i)
                flag[color[j]]=false;
        }
        int j=0;
        //cout<<i<<" and "<<flag[1]<<endl;
        for( j=0;j<4;j++)
        {
            if(flag[j])
            break;
        }
        color[i]=j;
        cout<<j+1;
    }
    //cout<<t+1<<endl;
 }