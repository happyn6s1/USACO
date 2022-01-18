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
#K=int(sys.stdin.readline().strip())
#N=int(NK[0])
#K=int(NK[1])
#M=int(NK[2])
#ol=list(map(int,sys.stdin.readline().strip().split()))
#d={0:0,1:0}

x=0
y=0
n,q=list(map(int,sys.stdin.readline().strip().split()))
st=list(map(int,sys.stdin.readline().strip().split()))
d={}
for i in range(n):
    if st[i] not in d:
        d[st[i]]=i+1
l=[]
for k in d:
    l.append([d[k],k])
l.sort()
ans=[]
ql=list(map(int,sys.stdin.readline().strip().split()))
for qq in ql:
    ans.append(str(d[qq]))
    t=d[qq]
    for k in d:
        if k==qq:
            d[k]=1
        elif d[k]<t:
            d[k]+=1

print(" ".join(ans))
