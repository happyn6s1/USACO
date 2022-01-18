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
int main()
{
    freopen("bcount.in","r",stdin);
    freopen("bcount.out","w",stdout);
    //vector<long long> a;
    //v<int> b;
    //cout<<"hell"<<endl;
    //cout<<recur(5);
    //return 0;
    long long  tt,a,b;
    int N,M;
    long long K;
    //int l[101];
    int nn[101];
    vector<int> g[101];
    cin>>N>>K;
    //cin>>a>>b;
    vector<long long> l[3];
    vector<long long> presum[3];
    presum[0].push_back(0);
    presum[1].push_back(0);
    presum[2].push_back(0);
    for(int i=0;i<N;i++)
    {
        //cout<<"h";
        cin>>a;
        int t[3]={0,0,0};
        t[a-1]+=1;
        presum[0].push_back(presum[0][i]+t[0]);
        presum[1].push_back(presum[1][i]+t[1]);
        presum[2].push_back(presum[2][i]+t[2]);
        //cout<<presum[0][i+1]<<endl;
    }
    //cout<<K;
    for(int i=0;i<K;i++)
    {
        cin>>a>>b;
        a-=1;
        //b-=1;
        cout<<presum[0][b]-presum[0][a];
        cout<<" ";
        cout<<presum[1][b]-presum[1][a];
        cout<<" ";
        cout<<presum[2][b]-presum[2][a];
        cout<<endl;

    }
    
 }