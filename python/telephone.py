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
NK=sys.stdin.readline().strip().split()
N=int(NK[0])
K=int(NK[1])
B=sys.stdin.readline().strip().split()
br=[[] for i in range(K)]
for i in range(N):
    B[i]=int(B[i])-1
    br[B[i]].append(i)
M=[]
#print(B,br)
g=[[] for i in range(K)]
for i in range(K):
    tl=[]
    sss=sys.stdin.readline().strip()
    for s in sss:
        if s=="0":
            tl.append(0)
        else:
            tl.append(1)
    M.append(tl)
for i in range(K):
    for j in range(K):
        if M[i][j]==1:
            g[i].append(j)
#print(g)
graph=[[] for i in range(N)]
weight=[MOD for i in range(N)]
'''
for i in range(N):
    for j in range(N):
        if j==i:
            continue
        #print(B,i,j,M)
        if M[B[i]][B[j]]==1:
            graph[i].append(j)
'''
#print(graph)
d={}
h=[]
for i in range(1,N):
    heapq.heappush(h,(MOD,i))
heapq.heappush(h,(0,0))
#print(h)
while h:
    w,p=heapq.heappop(h)
    weight[p]=w
    if p==N-1:
        break
    if p not in d:
        l=[]
        sss=set()
        for j in g[B[p]]:
            for jj in br[j]:
                if jj!=p:
                    sss.add(jj)
        d[p]=sss
    
    for t in d[p]:
        #print(p,t,weight[t],w)
        if w+abs(p-t)<weight[t]:
            #print(p,t)
            heapq.heappush(h,(w+abs(p-t),t))
    #print(h,p,d[p],weight,d)
print(weight[-1])
#print(ans)
#print(len(occupy))
