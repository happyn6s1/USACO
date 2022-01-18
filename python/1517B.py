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
for _ in range(K):
    ans=[]
    h=[]
    
    F=True
    n,m=list(map(int,sys.stdin.readline().strip().split()))
    hh=[[] for _ in range(n)]
    for j in range(n):
        st=list(map(int,sys.stdin.readline().strip().split()))
        for i in st:
            heapq.heappush(h,(i,j))
            heapq.heappush(hh[j],-i)
            
    
    for i in range(m):
        v,j=heapq.heappop(h)
        l=[0 for _ in range(n)]
        l[j]=v
        for k in range(n):
            if k==j:
                continue
            jj=-heapq.heappop(hh[k])
            l[k]=jj
        ans.append(l)
    for j in range(n):
        a=[]
        for i in range(m):
            a.append(str(ans[i][j]))
        print(" ".join(a))
        
