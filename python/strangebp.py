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
    d={}
    a=0
    b=0
    m,k=sys.stdin.readline().strip().split()
    m=int(m)
    k=int(k)
    ml=list(map(int,sys.stdin.readline().strip().split()))
    kl=list(map(int,sys.stdin.readline().strip().split()))
    dl=[0 for i in range(k)]
    for n in ml:
        dl[n-1]+=1
    start=0
    end=k-1
    ans=0
    while end>=0:
        if dl[end]>0:
            t=dl[end]
            while t>0:
                t-=1
                
                if end>start and kl[start]<kl[end]:
                    ans+=kl[start]
                    start+=1
                else:
                    ans+=kl[end]
        end-=1
        #print(end,ans)
    print(ans)
#for x,y in occupy:
#    l[x][y]="X"
#for ll in l:
#    print("".join(ll))

