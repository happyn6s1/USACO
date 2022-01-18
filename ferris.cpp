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
int main()
{
    //freopen("pairup.in","r",stdin);
    //freopen("pairup.out","w",stdout);
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
    
    vector<pair<long long, long long>> p;
    vector<long long> l;
    vector<long long> ll;
    vector<long long> tower;

    cin>>N>>M;
    //long long ans=-1000000;
    long long mmm=0;
    vector<long long> presum={0};
    //long long pre=0;
    // init all zeros
    //for(int i=0;i<2*N;i++)
     //   for(int j=0;j<2*N;j++)
     //       pp[i][j]=0;
    // tilted assign
    map<char,int> um;
    long long ans=0;
    //cin>>K;
    
    for(int i=0;i<N;i++)
    {
        cin>>a;
        l.push_back(a);
        
    }
    sort(l.begin(),l.end());
    
    
    int i=0;
    int j=l.size()-1;
    while(i<=j)
    {
        if(i==j)
        {
            ans+=1;
            break;
        }
        else if(l[i]+l[j]<=M)
        {
            ans+=1;
            i+=1;
            j-=1;
        }
        else
        {
            ans+=1;
            j-=1;
        }
    }
    cout<<ans;
 }