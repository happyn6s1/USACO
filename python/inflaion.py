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

for j in range(n):
    #l=[0]
    ans=0
    c=1.0
    pre=[0]
    #k=int(sys.stdin.readline().strip())
    AB=sys.stdin.readline().strip().split()
    N=int(AB[0])
    K=int(AB[1])
    L=sys.stdin.readline().strip().split()
    l=[]
    x=[1 for i in range(N)]
    for i in range(N):
        L[i]=int(L[i])
        l.append(L[i])
        pre.append(pre[-1]+L[i])
    #print(pre)
    for i in range(1,N):
        #print(L[i],pre[i],K,c)
        #if L[i]*100>pre[i]*K*c:
        #    a=L[i]*100/(pre[i]*K*c)
        #    c*=a
        x[i-1]=L[i]*100/K
    #print(x)
    for i in range(N):
        if x[i]>pre[i+1]:
            ans=max(ans,math.ceil(x[i]-pre[i+1]))
        #print(pre[i+1]*(x[i]-1),ans)
        
    #print(x,pre)
    print(ans)


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

