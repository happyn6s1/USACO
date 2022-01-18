"""
ID: happyn61
LANG: PYTHON3
PROB: loan
"""

#from collections import defaultdict
import sys

import heapq
import math
from collections import deque
MOD=1000000007
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]
def factor(n,l,d):
    F=False
    for p in l:
        if n%p==0:
            if p in d:
                d[p]+=1
            else:
                d[p]=1
            F=True
            break
    if F:
        factor(n//p,l,d)
            
#fin = open ('loan.in', 'r')
#fout = open ('loan.out', 'w')
#print(dic["4734"])
def find(parent,i):


    if parent[i] != i: 
        parent[i]=find(parent,parent[i]) 
    return parent[i] 

        # A utility function to do union of two subsets 
def union(parent,rank,xx,yy): 
    x=find(parent,xx)
    y=find(parent,yy)
    if rank[x]>rank[y]:
        parent[y]=x
    elif rank[y]>rank[x]:
        parent[x]=y
    else:
        parent[y]=x
        rank[x]+=1
ans=0

#NQ=sys.stdin.readline().strip().split()

n=int(sys.stdin.readline().strip())
#N1=int(NQ[0])
#N2=int(NQ[1])
#N3=int(NQ[1])
dd={"R":"L","L":"R"}
l=[0,0,1,1,3]
l=[-1 for i in range(n+2)]
l[0]=1000000
l[-1]=1000000

l=sys.stdin.readline().strip().split()
a=[-1]
b=[-1]
dp=[[[0,0,0] for j in range(2)] for i in range(n+1)] #weight and the other value
for i in range(1,n+1):
    for j in range(2):
        w1=w2=0
        w1=dp[i-1][j][0]
        w2=dp[i-1][1-j][0]
        #print(i,j,dp)
        if l[i-1] != dp[i-1][j][j+1]:
            w1+=1
        if l[i-1] !=dp[i-1][1-j][2-j]:
            w2+=1
        if w1>w2:
            dp[i][j]=[w1,-1,-1]
            dp[i][j][j+1]=l[i-1]
            dp[i][j][2-j]=dp[i-1][j][2-j]
        else:
            dp[i][j]=[w2,-2,-2]
            dp[i][j][2-j]=l[i-1]
            dp[i][j][j+1]=dp[i-1][1-j][j+1]
ans=0

print(max(dp[-1][0][0],dp[-1][1][0]))
n=0
#print(l[:20])
for testj in range(n):
    #l=[0]
    ans=-1
    c=1.0
    l=[]
    pre=[0]
    #stack=[("0",False)]
    ABN=sys.stdin.readline().strip().split()
    A=int(ABN[0])
    B=int(ABN[1])
    n=int(ABN[2])
    ma=sys.stdin.readline().strip().split()
    mhp=sys.stdin.readline().strip().split()
    F=False
    for i in range(n):
        if B<=0:
            F=True
            break
        ma[i]=int(ma[i])
        mhp[i]=int(mhp[i])
        l.append((ma[i],mhp[i]))
    l.sort()
    for i in range(n):
        ma=l[i][0]
        mhp=l[i][1]
        if B<=0:
            F=True
            break
        t=(mhp+A-1)//A
        if B<=(t-1)*ma:
            F=True
            break
        B-=(t*ma)
    #print(i,B,ma,mhp)
    if F:
        print("NO")
    else:
        print("YES")
    #AB=sys.stdin.readline().strip().split()
    #N=int(AB[0])
    #K=int(AB[1])

    #if k%4:
    #    print("NO")
    #else:
    #    print("YES")
    #print(ans)
    #print(" ".join(ans))
#    print("".join(l))
    #print(s)
    #l=sys.stdin.readline().strip().split()
    #s1=sys.stdin.readline().strip()
    #s2=sys.stdin.readline().strip()
    
        #print(pre,post,ll,rr,m1,m2,pre[ll],post[n-1-rr],post[n-1-rr][2])
    #if F:
    #    print("yes")
    #else:
    #    print("no")
    #return True
    
#for x,y in occupy:
#    l[x][y]="X"
#for ll in l:
#    print("".join(ll))

