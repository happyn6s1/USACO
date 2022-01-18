"""
ID: happyn61
LANG: PYTHON3
PROB: loan
"""
from itertools import product
import itertools
#from collections import defaultdict
import sys
import heapq
from collections import deque
MOD=1000000000007
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
#NK=sys.stdin.readline().strip().split()
K=int(sys.stdin.readline().strip())
#N=int(NK[0])
#K=int(NK[1])
#M=int(NK[2])
#ol=list(map(int,sys.stdin.readline().strip().split()))
#d={0:0,1:0}

x=0
y=0

#d={"N":(0,1),"S":(0,-1),"W":(-1,0),"E":(1,0)}
for testj in range(K):
    ans=0
    F=True
    N=int(sys.stdin.readline().strip())+2
    l=list(map(int,sys.stdin.readline().strip().split()))
    sm=sum(l)
    d={}
    for i in range(N):
        n=l[i]
        v=sm-n
        if v not in d:
            d[v]={i}
        else:
            d[v].add(i)
    F=False
    j=-1
    k=-1
    for i in range(N):
        n=l[i]
        #print(n*2,d,i)
        if n*2 in d:
            for t in d[n*2]:
                if t!=i:
                    j=i
                    k=t
                    F=True
                    break
            if F:
                break
    ans=[]
    if not F:
        print(-1)
        continue
    #print(d,k)
    for i in range(N):
        if i!=j and i!=k:
            ans.append(l[i])
    ans.sort()
    for i in range(len(ans)):
        ans[i]=str(ans[i])
    print(" ".join(ans))
