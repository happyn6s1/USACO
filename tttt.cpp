#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define vii vector<pair<int,int>> 
int main()
{
    freopen("tttt.in","r",stdin);
    freopen("tttt.out","w",stdout);
    int N;
//    cin>>N;
    vii speedlimit;
    vii driving;
    string a;
    char b[5];
    int pre=0;
    char M[3][3];
    for(int i=0;i<3;i++)
    {
        cin>>a;
        M[i][0]=a[0];
        M[i][1]=a[1];
        M[i][2]=a[2];
    }
    int p=0;
    int q=0;
    //cout<<M[0][0]<<endl;
   ///cout<<M[0][1]<<endl;
    set<char> A;
    set<pair<char,char>> B;

    for(int i=0;i<3;i++)
    {
        if(M[i][0]==M[i][1] and M[i][1]==M[i][2])
        {
            A.insert(M[i][0]);
        }
        else if (M[i][0]==M[i][1] or M[i][1]==M[i][2])
        {
            char m,n;
            m=M[i][0];
            n=M[i][2];
            if(m>n)
            {
                char t=n;
                n=m;
                m=t;
            }
            B.insert(make_pair(m,n));
        }
        else if (M[i][0]==M[i][2])
        {
            char m,n;
            m=M[i][0];
            n=M[i][1];
            if(m>n)
            {
                char t=n;
                n=m;
                m=t;
            }
            B.insert(make_pair(m,n));
        }
        
        if(M[0][i]==M[1][i] and M[1][i]==M[2][i])
             A.insert(M[0][i]);
        else if (M[0][i]==M[1][i] or M[1][i]==M[2][i])
        {
            char m,n;
            m=M[0][i];
            n=M[2][i];
            if(m>n)
            {
                char t=n;
                n=m;
                m=t;
            }
            B.insert(make_pair(m,n));
        }
        else if (M[0][i]==M[2][i])
        {
            char m,n;
            m=M[0][i];
            n=M[1][i];
            if(m>n)
            {
                char t=n;
                n=m;
                m=t;
            }
            B.insert(make_pair(m,n));
        }
        
        
        
    }
    if(M[0][0]==M[1][1] and M[1][1]==M[2][2])
        A.insert(M[0][0]);
    else if (M[0][0]==M[1][1] or M[1][1]==M[2][2])
    {
            char m,n;
            m=M[0][0];
            n=M[2][2];
            if(m>n)
            {
                char t=n;
                n=m;
                m=t;
            }
            B.insert(make_pair(m,n));
        }
        else if (M[0][0]==M[2][2])
        {
            char m,n;
            m=M[0][0];
            n=M[1][1];
            if(m>n)
            {
                char t=n;
                n=m;
                m=t;
            }
            B.insert(make_pair(m,n));
        }

    if(M[0][2]==M[1][1] and M[1][1]==M[2][0])
        A.insert(M[0][2]);
    else if (M[0][2]==M[1][1] or M[1][1]==M[2][0])
    {
            char m,n;
            m=M[0][2];
            n=M[2][0];
            if(m>n)
            {
                char t=n;
                n=m;
                m=t;
            }
            B.insert(make_pair(m,n));
        }
        else if (M[0][2]==M[2][0])
        {
            char m,n;
            m=M[0][2];
            n=M[1][1];
            if(m>n)
            {
                char t=n;
                n=m;
                m=t;
            }
            B.insert(make_pair(m,n));
        }

    
    cout<<A.size()<<endl;
    cout<<B.size()<<endl;
}