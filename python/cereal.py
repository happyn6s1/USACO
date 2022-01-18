"""
ID: happyn61
LANG: PYTHON3
PROB: cereal
"""
FN="cereal"
import collections,heapq
from collections import deque
import sys
INF=999999
AL="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
al="abcdefghijklmnopqrstuvwxyz"
cost={}
visited=set()
hcost=[]
d={}

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
def fit(n,ol,limit):
    k=0
    i=0
    F=True
    p=-1
    while i<len(ol):
        if F:
            p=ol[i][0]
            F=False
            k+=1
            
        else:
            if p+n<=ol[i][1]:
                #print(ol[i],p,n)
                ps=max(p+n,ol[i][0])
                m=(ol[i][1]-ps)//n+1
                p=ps+m*n-n
                k+=m
                i+=1
            else:
                i+=1
        if k>=limit:
            #print(n)
            return True
    return False
                
ans=0
BIG=1000
fin = open (FN+'.in', 'r')
fout = open (FN+'.out', 'w')
#N=int(fin.readline().strip())
MN=fin.readline().strip().split()
N=int(MN[0])
M=int(MN[1])
    #print(ans)
ol=[]
ct=0
x=[]
y=[]
l=[deque([]) for i in range(M)]
lc=[[] for i in range(N)]
for i in range(N):
    f,s=fin.readline().strip().split()
    f=int(f)
    s=int(s)
    l[f-1].append(i)
    l[s-1].append(i)
    lc[i]=[f-1,s-1]

s=set()
for i in range(0,N):
    while (l[lc[i][0]][0],0) in s:
        l[lc[i][0]].popleft()
    while (l[lc[i][1]][0],1) in s:
        l[lc[i][1]].popleft()
    if l[lc[i][0]][0]==i:
        ans+=1
        s.add((i,1))
    elif l[lc[i][1]][0]==i:
        ans+=1
        s.add((i,0))
    #print(i,s,l)
print(ans)
for i in range(1,N):
    ans-=1
    if l[lc[i][0]] and l[lc[i][0]][0]==i:
        l[lc[i][0]].popleft()
        if l[lc[i][0]]:
            ans+=1
            t=l[lc[i][0]][0]
            s.add((i,0))
fout.write(str(ans)+"\n")            
fout.close()
