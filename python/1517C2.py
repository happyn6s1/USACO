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

M=[[-1]*K for _ in range(K)]
for i in range(K):
    for j in range(K):
        if j<=i:
            M[i][j]=0

FF=False

ol=list(map(int,sys.stdin.readline().strip().split()))

for it in range(K):
    M[it][it]=ol[it]
    v=ol[it]-1
    vv=ol[it]
    hh=[]
    j=it
    #print(it,ol,v,vv,M)
    for ii,jj in ((1,0),(-1,0),(0,1),(0,-1)):
        #print(ii,jj,it+ii,
        if it+ii>=0 and it+ii<K and j+jj>=0 and j+jj<K and M[it+ii][j+jj]==0:
            heapq.heappush(hh,(j+jj,it+ii))
    for t in range(v):
        #print(it,t,hh,v)
        if len(hh)==0:
            FF=True
            print(M)
            break
        j,i=heapq.heappop(hh)
        M[i][j]=vv
        for ii,jj in ((1,0),(-1,0),(0,1),(0,-1)):
            if i+ii>=0 and i+ii<K and j+jj>=0 and j+jj<K and M[i+ii][j+jj]==0:
                heapq.heappush(hh,(j+jj,i+ii))
    if FF:
        break

if FF:
    print(-1)
else:
    #print(M)
    
    for i in range(K):
        ans=[]
        for j in range(i+1):
            ans.append(str(M[i][j]))
        print(" ".join(ans))
    #print(f"\n")
