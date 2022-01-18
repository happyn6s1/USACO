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
#M=int(NK[2])
ans=[{i} for i in range(N)]
aset=[{i} for i in range(N)]
ab=[i for i in range(N)]
p=[i for i in range(N)]
k=[]
for i in range(K):
    A,B=sys.stdin.readline().strip().split()
    A=int(A)-1
    B=int(B)-1

    k.append((A,B))
#print(k)
for i in range(K):
    kk=i
    A=k[kk][0]
    B=k[kk][1]
    t=p[B]
    p[B]=p[A]
    p[A]=t
    aset[p[A]].add(A)
    aset[p[B]].add(B)
    ab[p[A]]=A
    ab[p[B]]=B
    #print(A,B)
    #print(p,ab,aset)
#print(p)
pp=[-1 for i in range(N)]
for i in range(N):
    pp[p[i]]=i
ans=[-1 for i in range(N)]
visited=[False for i in range(N)]
for i in range(N):
    if visited[i]:
        continue
    visited[i]=True
    pi=pp[i]
    l=[i]
    while pi!=i:
        l.append(pi)
        visited[pi]=True
        pi=pp[pi]
    ss=set()
    k=2000
    for t in l:
        ss=ss.union(aset[t])
        k-=1
        if k<0:
            break
    for t in l:
        ans[t]=len(ss)
for i in range(N):
    print(ans[i])
#print(ans)
#print(len(occupy))
