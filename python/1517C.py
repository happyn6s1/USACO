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
W=[[0]*K for _ in range(K)]
#print(M,W)
for i in range(K):
    for j in range(K):
        if M[i][j]<0:
            continue
        for ii,jj in ((1,0),(-1,0),(0,1),(0,-1)):
            if i+ii>=0 and i+ii<K and j+jj>=0 and j+jj<K and M[i+ii][j+jj]>=0:
                W[i][j]+=1
        if i==K-1:
            W[i][j]+=1
        if j==0:
            W[i][j]+=1

h=[]
FF=False
def adm(i,j):
    W[i][j]=0
    for ii,jj in ((1,0),(-1,0),(0,1),(0,-1)):
        if i+ii>=0 and i+ii<K and j+jj>=0 and j+jj<K and M[i+ii][j+jj]>=0:
            W[i+ii][j+jj]-=1
ol=list(map(int,sys.stdin.readline().strip().split()))
for i in range(K):
    heapq.heappush(h,(ol[i],i))
    M[i][i]=ol[i]
while h:
    v,i=heapq.heappop(h)
    hh=[]
    vv=v
    M[i][i]=vv
    j=i
    for ii,jj in ((1,0),(-1,0),(0,1),(0,-1)):
        if i+ii>=0 and i+ii<K and j+jj>=0 and j+jj<K and M[i+ii][j+jj]==0:
            heapq.heappush(hh,(W[i+ii][j+jj],i+ii,j+jj))
    adm(i,i)
    #print(M,W,v,hh)
    while v>1:
        F=False
        while hh:
            w,i,j=heapq.heappop(hh)
            #print(w,i,j,M,W)
            if M[i][j]==0:
                M[i][j]=vv
                #print(vv,M,W,i,j)
                v-=1
                adm(i,j)
                for ii,jj in ((1,0),(-1,0),(0,1),(0,-1)):
                    if i+ii>=0 and i+ii<K and j+jj>=0 and j+jj<K and M[i+ii][j+jj]==0:
                        heapq.heappush(hh,(W[i+ii][j+jj],i+ii,j+jj))
                F=True
                break
        if not F:
            FF=True
            break
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
