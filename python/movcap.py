"""
ID: happyn61
LANG: PYTHON3
PROB: loan
"""

#from collections import defaultdict
import sys
import heapq
from collections import deque

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
#N=int(NQ[0])
#D=int(NQ[1])
for i in range(n):
    _=sys.stdin.readline()
    d={}
    a=0
    b=0
    m,k=sys.stdin.readline().strip().split()
    m=int(m)
    k=int(k)
    g=[[]for i in range(m)]
    rg=[[]for i in range(m)]
    ds=[-1 for i in range(m)]
    rds=[m+1 for i in range(m)]
    for j in range(k):
        #ans=[]
        
        K=sys.stdin.readline().strip().split()
        a=int(K[0])
        b=int(K[1])
        a=int(a)-1
        b=int(b)-1
        #print(m,k,a,b)
        g[a].append(b)
        rg[b].append(a)
    #print(g)
    visited=[False for i in range(m)]
    dq=deque([[0,0]])
    visited[0]=True
    while dq:
        i,w=dq.popleft()
        #print(tt)
        ds[i]=w
        w+=1
        for t in g[i]:
            if not visited[t]:
                dq.append([t,w])
                visited[t]=True

        #print(dq,visited,g)
    visited=[False for i in range(m)]
    dq=deque([[0,0]])
    visited[0]=True
    while dq:
        i,w=dq.popleft()
        #print(i,w)
        rds[i]=w
        
        
        for t in rg[i]:
            if not visited[t]:
                if ds[t]<ds[i] :
                    ww=w
                else:
                    ww=w+1
                dq.append([t,ww])
                visited[t]=True
    l=[0]
    print(ds,rds)
    for i in range(1,m):
        l.append(min(ds[i],rds[i]-1))
    for i in range(m):
        l[i]=str(l[i])
    print(" ".join(l))
#for x,y in occupy:
#    l[x][y]="X"
#for ll in l:
#    print("".join(ll))

